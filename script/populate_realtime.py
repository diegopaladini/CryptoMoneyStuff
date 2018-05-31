#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 15:48:59 2018

@author: Legnani
"""

from poloniex import Poloniex
import pandas as pd
from pandas import DataFrame
from datetime import datetime
from sqlalchemy import create_engine



def populate_prices(cur_pair, instance, end_date, connection):
    
    for tag, cur in cur_pair.items():
        print('>>> Request for pair', cur)
        
        sql = ("select max(timestamp) from cryptos.prices where currency_pair='" + cur + "'")
        result = connection.execute(sql).fetchall()       
        dum_df = DataFrame(result, columns = ['last_date'])
        
        if dum_df.isnull().bool():
            last_date = datetime(2011,1,1,0,0)
        else:
            last_date = dum_df.iloc[0]['last_date']
        del dum_df
        
        print('   ...last date found on db: %s' %last_date)
        raw = instance.returnChartData(cur, period=300, start=datetime.timestamp(last_date)+1, end=datetime.timestamp(end_date))
        
        df = pd.DataFrame(raw)
        
        df['date'] = df['date'].apply(lambda x: datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
           
        todb = DataFrame()
        todb['timestamp'] = df['date']
        todb['exchange'] = 'poloniex'
        todb['currency_pair'] = cur
        todb['currency_tag'] = tag
        todb['open'] = df['open']
        todb['close'] = df['close']
        todb['high'] = df['high']
        todb['low'] = df['low']
        todb['weighted_average'] = df['weightedAverage']
        todb['base_volume'] = df['volume']
        todb['quote_volume'] = df['quoteVolume'] 
        
        todb.drop_duplicates(inplace = True)
        
        print('   ...got %d records from poloniex' %len(todb))
        print('   ...start inserting into db')              
        for row in todb.iterrows():
            dum = DataFrame(row[1])
            try:
                dum.transpose().to_sql('prices', connection, if_exists='append', schema='cryptos', index=False)
            except:
                print('   ___ Errore caricamento DB ___')
                pass #or any other 
            
 
    return 0






def main():

    # Define the currencies of interest and their tag
    cur_pair = {'stellar':'BTC_STR', 'ripple':'BTC_XRP', 'bitcoin':'USDT_BTC'}
    
    # Read credentials for db connection
    credentials_db = pd.read_csv('..\\credentials\\db.cred', sep=';', encoding='UTF8', header=None, index_col=0)

    db = credentials_db.loc['db'][1]
    user = credentials_db.loc['user'][1]
    pwd = credentials_db.loc['pwd'][1]
    
    # Create db engine and connection
    engine = create_engine('postgresql://' + user + ':' + pwd + '@' + db + ':5432/postgres')
    connection = engine.connect()
    

    # Read credentials for Poloniex API
    credentials_polo = pd.read_csv('..\\credentials\\poloniex.cred', sep=';', encoding='UTF8', header=None, index_col=0)

    # Create Poloniex API instance
    instance = Poloniex(credentials_polo.loc['apikey'][1], credentials_polo.loc['secret'][1])

    
    end_date = datetime(2025,1,20,15,15)

    
    # Populate prices table
    populate_prices(cur_pair, instance, end_date, connection)

    # Close connection to db
    connection.close()
    engine.dispose()
    
    return





if __name__ == '__main__':
    try:
        main()
    except:
        pass






    