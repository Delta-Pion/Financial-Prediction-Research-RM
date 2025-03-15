import yfinance as yf
import pandas as pd

# Basic Setup
## reliance = yf.Ticker("RELIANCE.NS")
## reliance_historical = reliance.history(period="1mo")
## print(reliance_historical)

# How to Download
## data = yf.download("RELIANCE.NS BAJFINANCE.NS ADANIENT.NS", start="2025-01-01", end="2025-02-30")
## print(data)

# Multi Ticker
## data = yf.Tickers("RELIANCE.NS BAJFINANCE.NS ADANIENT.NS")
## data_history = data.history(period="1y", group_by="tickers")
## print(data_history)

# Ticker Info
## print(reliance.info['dividendRate'])
## print(reliance.info['forwardPE'])
## print(reliance.dividends)

# Fundamentals data with multiple tickers at once

tickers_list = ["RELIANCE.NS", "BAJFINANCE.NS", "ADANIENT.NS"] # example list
tickers_data= {}

for ticker in tickers_list:
    ticker_object = yf.Ticker(ticker)

    #convert info() output from dictionary to dataframe
    temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
    temp.reset_index(inplace=True)
    temp.columns = ["Attribute", "Recent"]
    
    # add (ticker, dataframe) to main dictionary
    tickers_data[ticker] = temp

#print(tickers_data)

combined_data = pd.concat(tickers_data)
combined_data = combined_data.reset_index()
combined_data

del combined_data["level_1"] # clean up unnecessary column
combined_data.columns = ["Ticker", "Attribute", "Recent"] # update column names

#print(combined_data)

employees = combined_data[combined_data["Attribute"]=="fullTimeEmployees"].reset_index()
#print(employees)

employees_sorted = employees.sort_values('Recent',ascending=False)
print(employees_sorted)
