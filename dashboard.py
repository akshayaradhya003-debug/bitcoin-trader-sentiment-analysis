import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("processed_trading_data.csv")

st.title("Bitcoin Trader Sentiment Dashboard")

st.subheader("Dataset Preview")
st.dataframe(data.head())

# PnL distribution
st.subheader("PnL Distribution")
fig, ax = plt.subplots()
sns.histplot(data['Closed PnL'], bins=30, ax=ax)
st.pyplot(fig)

# Long vs Short
st.subheader("Long vs Short Trades")
side_counts = data['Side'].value_counts()
st.bar_chart(side_counts)

# Trade Size
st.subheader("Trade Size Distribution")
fig2, ax2 = plt.subplots()
sns.boxplot(data=data, y='Size USD', ax=ax2)
st.pyplot(fig2)

