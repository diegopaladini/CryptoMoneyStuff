#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 14:47:53 2018

@author: Legnani
"""

from poloniex import Poloniex
import pandas as pd
from pandas import DataFrame
from datetime import datetime
from sqlalchemy import create_engine


instance = Poloniex('Y9IB73CC-JAGTQ05O-UD94HHDI-69HJ09BO',
                  '3a2a015f5d483c5e7e3971bd70064818e4dc5f8e8e4bd5abfc732d18519131a510ab43b576bf43a911a001421564517f77508396d36308e6c3132825edbae935')

#cur_pair = {'stellar':'BTC_STR', 'ripple':'BTC_XRP'}
cur_pair = {'bitcoin':'USDT_BTC'}

start_date = datetime(2011,1,1,0,0)
end_date = datetime(2018,1,20,23,59)

for tag, cur in cur_pair.items():
    
    print('>>> Request for pair', cur)
    
    raw = instance.returnChartData(cur, period=300, start=start_date, end=end_date)
    
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
    
    print('...loading to Postgres', cur)
    engine = create_engine('postgresql://postgres:112358@localhost:5432/dbo')

#    try:
#        todb.to_sql('prices', engine, if_exists='append', schema='cryptos', index=False, chunksize = 1)
#    except:
#        print('### Errore caricamento DB ###')
#        pass #or any other actio

    for row in todb.iterrows():
        dum = DataFrame(row[1])
        try:
            dum.transpose().to_sql('prices', engine, if_exists='append', schema='cryptos', index=False)
        except:
            print('### Errore caricamento DB ###')
            pass #or any other action
            