SELECT 
cp.timestamp, cp.open, cp.close, cp.high, cp.low, cp.weighted_average, cp.base_volume, cp.quote_volume,
cp5.open, cp5.close, cp5.high, cp5.low, cp5.weighted_average, cp5.base_volume, cp5.quote_volume,
cpt.close

FROM cryptos.prices AS cp,
cryptos.prices AS cp5,
cryptos.prices AS cpt

WHERE cp.currency_pair = 'BTC_XRP'
AND cp5.currency_pair = cp.currency_pair
AND cpt.currency_pair = cp.currency_pair
AND cp5.timestamp + interval '5 minute' = cp.timestamp
AND cpt.timestamp - interval '5 minute' = cp.timestamp
AND cp.timestamp > '2015-12-31'
ORDER BY cp.timestamp