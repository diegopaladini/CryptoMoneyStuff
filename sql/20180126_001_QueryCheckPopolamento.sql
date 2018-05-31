SELECT currency_pair, MIN(timestamp), MAX(timestamp), COUNT(*) 
FROM cryptos.prices
GROUP BY currency_pair, date_part('year', timestamp)