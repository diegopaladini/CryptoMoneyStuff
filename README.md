# CryptoMoneyStuff

## Folders
* script: contains project scripts (Python 3.5)
	* algo: scripts for trading algorithms definition
	* data: scripts for data management (download from Polniex and insert into db).
	* forecast: scripts for up/down forecasting (classification).
	* models: saved models
* credentials: contains files with login credentials. Not pughed to git.
* sql: contains useful queries
* sh: some .sh test scripts


# To Do
## Data
* download data about Order Book: returnOrderBook API. Define time interval of data update and for which currencies.
* download data about Volumes: return24hVolume API. Define time interval of data update and for which currencies.
* populate table about fees (handmade)

## Forecasting
* define what to forecast (target): binary classification of up/sell, price regression
* define time horizon of the forecast
* define features used to forecast/which currencies

## Trading
* define trading algo
* define on which currencies to focus
* arbitrage opportunity between different trading desks

