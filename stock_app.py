import yfinance as yf
import numpy as np
import streamlit as st

def download_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def calculate_metrics(stock_data, column='Close'):
    prices = stock_data[column]

    # Calculate standard deviation
    std_deviation = np.std(prices)

    # Calculate mean
    mean_price = np.mean(prices)

    # Calculate daily returns
    daily_returns = prices.pct_change().dropna()

    # Assume risk-free rate as 0 for simplicity
    risk_free_rate = 0

    # Calculate Sharpe ratio
    sharpe_ratio = (np.mean(daily_returns) - risk_free_rate) / np.std(daily_returns)

    return std_deviation, mean_price, sharpe_ratio, daily_returns

def main():
    st.title("Stock Metrics Calculator")

    # Get user input
    stock_ticker = st.text_input("Enter the stock ticker:")
    start_date = st.text_input("Enter the start date (YYYY-MM-DD):", "2018-01-01")
    end_date = st.text_input("Enter the end date (YYYY-MM-DD):", "2023-01-01")

    if st.button("Calculate"):
        # Download historical stock data
        stock_data = download_stock_data(stock_ticker, start_date, end_date)

        if stock_data.empty:
            st.warning(f"No data available for {stock_ticker} in the specified date range.")
        else:
            # Calculate metrics
            std_deviation, mean_price, sharpe_ratio, daily_returns = calculate_metrics(stock_data)

            # Display the result
            st.success(f"Standard Deviation of {stock_ticker} stock prices: {std_deviation}")
            st.success(f"Mean of {stock_ticker} stock prices: {mean_price}")
            st.success(f"Sharpe Ratio of {stock_ticker} stock: {sharpe_ratio}")

            # Display line chart of historical stock prices
            st.write("Historical Stock Prices:")
            st.line_chart(stock_data['Close'])

            # Optionally, you can display the stock data as a table
            st.write("Historical Stock Data:")
            st.write(stock_data)

if __name__ == "__main__":
    main()

