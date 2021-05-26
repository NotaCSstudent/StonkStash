import yfinance as yf


Stock = yf.Ticker("AAPL")
History = Stock.history(period="max")
print(History)