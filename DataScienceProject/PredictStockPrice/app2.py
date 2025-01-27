import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

start = '2015-01-01'
end = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction Application")

# stock = ("AAPL","GOOG")

selectedStock = st.text_input('Enter Stock Symbol',"AAPL")
# selectedStock = st.selectbox("Select Dataset",stock)

nYears = st.slider("Years Prediction: ",1,4)
period = nYears * 365

@st.cache_data
def load_data(ticker):
    df = yf.download(ticker,start,end)
    df.reset_index(inplace=True)
    df.columns = df.columns.get_level_values(0)
    return df

dataLoad = st.markdown("Load data...")
data = load_data(selectedStock)
dataLoad.markdown(":green[Loading data done!]")

st.subheader("Raw Data")
st.write(data.tail())

def plot_raw():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = data['Date'], y = data['Open'], name = 'Stock Open',line=dict(color='green') ))
    fig.add_trace(go.Scatter(x = data['Date'], y = data['Close'], name = 'Stock Close',line=dict(color='red') ))
    fig.layout.update(title = 'Time Series Data', xaxis_rangeslider_visible = True)
    st.plotly_chart(fig)

plot_raw()

dfTrain = data[['Date','Close']]
dfTrain = dfTrain.rename(columns ={"Date" : 'ds', "Close": "y"})

m = Prophet()
m.fit(dfTrain)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader("Forecast Data")
st.write(forecast.tail())

st.write('Forecast Data')
fig1 = plot_plotly(m,forecast)
st.plotly_chart(fig1)

st.write("Forecast Components")
fig2 = m.plot_components(forecast)
st.write(fig2)