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
from sqlalchemy import text


def populate(cur_pair, instance, end_date, connection):
    
    for tag, cur in cur_pair.items():
        print('>>> Request for pair', cur)
        sql = text(("select max(timestamp) from cryptos.prices where currency_pair='" + cur + "'"))
        
        result = connection.execute(sql)
        for row in result:
            last_date = row[0]
        
        raw = instance.returnChartData(cur, period=300, start=datetime.timestamp(last_date)+1, end=end_date)
        
        df = pd.DataFrame(raw)
        
        df.date = df.date.apply(lambda x: datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
           
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
        
        todb.drop_duplicates()
        
            
        for row in todb.iterrows():
            dum = DataFrame(row[1])
            try:
                dum.transpose().to_sql('prices', connection, if_exists='append', schema='cryptos', index=False)
            except:
                print('### Errore caricamento DB ###')
                return 0 #or any other 
            
            

        
            
    return 0





 


def main():
      
    cur_pair = {'stellar':'BTC_STR', 'ripple':'BTC_XRP', 'bitcoin':'USDT_BTC'}

	credentials_db = read_csv('..\\credentials\\db.cred', sep=';', encoding='UTF8', header=None, index_col=0)

	db = credentials_db.loc['db'][1]
	user = credentials_db.loc['user'][1]
	pwd = credentials_db.loc['pwd'][1]
	
	credentials_polo = read_csv('..\\credentials\\poloniex.cred', sep=';', encoding='UTF8', header=None, index_col=0)

	apikey = credentials_db.loc['apikey'][1]
	secret = credentials_db.loc['secret'][1]
	
	
	
	
    engine = create_engine('postgresql://' + user + ':' + pwd + '@' + db + ':5432/dbo')
    connection = engine.connect()
    instance = Poloniex(apikey, secret)
    
    end_date = datetime(2025,1,20,15,15)

    
    populate(cur_pair, instance, end_date, connection)
    
    connection.close()
    engine.dispose()
    
    return
    

    
if __name__ == '__main__':
    try:
        main()
    except:
        pass






    