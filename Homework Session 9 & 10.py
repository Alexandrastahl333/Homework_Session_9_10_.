
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Define the ticker symbols for the companies
tickers = ['PUM.DE', 'NKE', 'LULU']  # Puma, Nike, Lululemon

# Download stock data
data = yf.download(tickers, start='2022-01-01', end='2023-01-01')['Adj Close']

# Convert 'Date' columns to datetime and set as index (handled by yfinance)
# Align the data by date
aligned_data = data

# Plotting the adjusted close prices
plt.figure(figsize=(14, 7))
plt.plot(aligned_data['PUM.DE'], label='Puma')
plt.plot(aligned_data['NKE'], label='Nike')
plt.plot(aligned_data['LULU'], label='Lululemon')
plt.title('Adjusted Close Prices of Puma, Nike, and Lululemon')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend()
plt.grid(True)
plt.show()

# Calculate the correlation matrix
correlation_matrix = aligned_data.corr()
print(correlation_matrix)
