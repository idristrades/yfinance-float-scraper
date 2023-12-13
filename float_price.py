import yfinance as yf
import pandas as pd
from time import time

symbol = input('Enter ticker symbol:')

start = time()

try:
	ticker = yf.Ticker(symbol).upper()

	share_float = str('float = M'), round(ticker.info['floatShares'] / 1000000, 1)
	price = str('price = $'), round(ticker.info['currentPrice'] / 1, 2)

	df = pd.DataFrame([share_float, price])
	print(df)
except:
    print('No data returned for this ticker')

end = time()
print('Time taken: ' + str(round(end - start, 2)) + 's')
