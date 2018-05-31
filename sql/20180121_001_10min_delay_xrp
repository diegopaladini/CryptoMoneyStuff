SELECT 
cp.timestamp, cp.open, cp.close, cp.high, cp.low, cp.weighted_average, cp.base_volume, cp.quote_volume,
cp5.open, cp5.close, cp5.high, cp5.low, cp5.weighted_average, cp5.base_volume, cp5.quote_volume,
cp10.open, cp10.close, cp10.high, cp10.low, cp10.weighted_average, cp10.base_volume, cp10.quote_volume,
cpt.close

FROM cryptos.prices AS cp,
cryptos.prices AS cp5,
cryptos.prices AS cp10,
cryptos.prices AS cpt

WHERE cp.currency_pair = 'BTC_XRP'

AND cp5.currency_pair = cp.currency_pair
AND cp10.currency_pair = cp.currency_pair
AND cpt.currency_pair = cp.currency_pair

AND cp5.timestamp + interval '5 minute' = cp.timestamp
AND cp10.timestamp + interval '10 minute' = cp.timestamp
AND cpt.timestamp - interval '5 minute' = cp.timestamp

AND cp.timestamp > '2015-12-31'

ORDER BY cp.timestamp