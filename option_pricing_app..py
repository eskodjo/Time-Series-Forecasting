import streamlit as st
import numpy as np
from scipy.stats import norm

def black_scholes_option_price(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return option_price

def main():
    st.title("Black-Scholes Option Pricing Calculator")

    st.sidebar.header("Input Parameters")

    S = st.sidebar.number_input("Current Stock Price (S)", value=100.0)
    K = st.sidebar.number_input("Strike Price (K)", value=100.0)
    T_days = st.sidebar.number_input("Time to Maturity (T) in days", value=365)
    T_years = T_days / 365.0
    r = st.sidebar.number_input("Risk-Free Rate (r)", value=0.05)
    sigma = st.sidebar.number_input("Volatility (sigma)", value=0.2)

    option_type = st.sidebar.radio("Option Type", ['Call', 'Put'])

    if option_type == 'Call':
        option_type = 'call'
    elif option_type == 'Put':
        option_type = 'put'

    option_price = black_scholes_option_price(S, K, T_years, r, sigma, option_type)

    st.subheader("Option Price:")
    st.write(f"The calculated {option_type.capitalize()} option price is: ${option_price:.2f}")

if __name__ == "__main__":
    main()
