import streamlit as st
import yfinance as finance


def get_ticker(name):
	company = finance.Ticker(name) # companies
	return company


# Project Details
st.title("Build and Deploy Stock Market App Using Streamlit and python")
st.header("by Juan Peralta")
st.sidebar.header("Advanced Computing \n Spring 2023")

company1 = get_ticker("SONY")
company2 = get_ticker("NTDOY")

# fetches the data: Open, Close, High, Low and Volume
sony = finance.download("SONY", start="2023-05-04", end="2023-05-04")
nintendo = finance.download("NTDOY", start="2023-05-04", end="2023-05-04")

# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
data1 = company1.history(period="6mo")
data2 = company2.history(period="6mo")

# markdown syntax
st.write("""
### SONY
""")

# detailed summary on Google
st.write(company1.info['longBusinessSummary'])
st.write(sony)

# plots the graph
st.line_chart(data1.values)

st.write("""
### Nintendo
""")
st.write(company2.info['longBusinessSummary'], "\n", nintendo)
st.line_chart(data2.values)
