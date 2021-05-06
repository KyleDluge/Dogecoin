#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 11:24:54 2021

@author: kyledluge
"""
#Analysis of Dogecoin for 2021

import datetime as dt
from datetime import date
import streamlit as st
import yfinance as yf
from plotly import graph_objs as go

from fbprophet import Prophet
import prophet as pt
from prophet.plot import plot_plotly


start = dt.datetime(2021,1,1)
today = date.today().strftime('%Y-%m-%d')



st.title('Crypto Predictionator 2021')
stocks = ('Doge-USD', 'BTC-USD', 'ETH-USD')
selected_stocks = st.selectbox('Select coin', stocks)
n_months = st.slider('months', 1, 4)
period = n_months * 12


@st.cache
def load_data(ticker):
    data = yf.download(ticker, start, today)
    data.reset_index(inplace=True)
    return data


#LOADING STATE

data_load_state = st.text("Loading Crypto Data...")
data = load_data(selected_stocks)
data_load_state.text("Crypto Data Loaded Successfully")
data_load_state1 = st.text("Loading Crypto Predictions...")
data = load_data(selected_stocks)
data_load_state1.text("Crypto Predictions Loaded Successfully")


#DATA PLOT
    
st.subheader("Raw Data")
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Stock Open'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Stock Close'))
    fig.layout.update(title_text='Cyrpto Open/Close', xaxis_rangeslider_visible=True)   
    st.plotly_chart(fig)

plot_raw_data()



#CYRPTO PREDICTIONS


df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close":"y"})


m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

    
st.subheader("CRYPTO PREDICTIONS")
st.write(forecast.tail())


#PREDICTIONS PLOT


st.write("Prediction Data")
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)


st.write("Prediction Components")

fig2 = m.plot_components(forecast)
st.write(fig2)













