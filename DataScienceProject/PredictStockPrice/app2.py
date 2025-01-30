import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
import altair as alt
import pandas as pd
from PIL import Image
import requests

# Configure the page layout to be wider
st.set_page_config(layout="wide")

# Application title
st.title("📈 Stock Prediction Application with Prophet and Altair")
st.markdown("""
This application allows you to visualize historical stock data, perform future price predictions using Facebook's Prophet model, and stay updated with the latest news related to your selected stock.
""")

# Sidebar for user input
st.sidebar.header("🔍 User Input")

# Input for stock symbol
selectedStock = st.sidebar.text_input('Enter Stock Symbol', "AAPL").upper()

# Slider to select prediction years
nYears = st.sidebar.slider("Prediction Years: ", 1, 4, 1) # begin, end, step
period = nYears * 365

# Define start and end dates
start = '2015-01-01'
end = date.today().strftime("%Y-%m-%d")

# function to load a data form yahoo finance
@st.cache_data
def load_data(ticker):
    """
    Function to fetch stock data from Yahoo Finance.
    """
    df = yf.download(ticker, start, end)
    if df.empty:
        st.error("Data not found. Please check the entered stock symbol in Yahoo Finance😊.")
        return pd.DataFrame()
    df.reset_index(inplace=True)
    df.columns = df.columns.get_level_values(0)
    return df

# function to load info from yahoo finance
@st.cache_data
def load_information(ticker):
    """
    fucntion to fetch information about stock from Yahoo finance
    """
    info = yf.Ticker(ticker)
    info = info.info
    return info

@st.cache_data
def load_financials(ticker):
    """
    function to fetch financials information about that stock
    """
    fnc = yf.Ticker(ticker)
    fnc = fnc.get_financials()
    return fnc

@st.cache_data
def load_calls(ticker):
    call = yf.Ticker(ticker)
    call = call.option_chain()
    return call.calls

@st.cache_data
def load_puts(ticker):
    puts = yf.Ticker(ticker)
    puts = puts.option_chain()
    return puts.puts

@st.cache_data
def load_institutional_holders(ticker):
    """
    function to fetch information about institutional holders of that stock
    """
    tck = yf.Ticker(ticker)
    tck = tck.institutional_holders
    return tck


# Load Information
info = load_information(selectedStock)
if info:
    st.subheader(f"🏢 Company Information : {info.get('longName', 'N/A')}") # input, handle
    # company_officers = info.get('companyOfficers', [])
    # ceo_info = company_officers[0]

    col1, col2 = st.columns([1,2])  
    with col1:

        metrics = {
            # "Owner": ceo_info.get(f'name',"N/A"),
            "Country": info.get('country', "N/A"),
            "Sector": info.get('sector', 'N/A'),
            "Industry": info.get('industry', "N/A"),
        }

        # Check and extract CEO's name
        company_officers = info.get('companyOfficers', [])
        if isinstance(company_officers, list) and len(company_officers) > 0:
            ceo_info = company_officers[0]  # Assuming the first officer is the CEO
            metrics["CEO"] = ceo_info.get('name', 'N/A')

            # Optional: Extract CFO's name
            for officer in company_officers:
                if officer.get('title', '').lower().startswith('cfo'):
                    metrics["CFO"] = officer.get('name', 'N/A')
                    break  # Stop after finding the CFO

            # Optional: Extract Board Members' names
            board_members = [officer.get('name', 'N/A') for officer in company_officers if 'director' in officer.get('title', '').lower()]
            if board_members:
                metrics["Board Members"] = ", ".join(board_members)

        for key, value in metrics.items():
                st.write(f"**{key}:** {value}")
    with col2:
        metrics = {
            "Market Cap": f"${info.get('marketCap', 'N/A'):,}",
            "52 Week High": f"${info.get('fiftyTwoWeekHigh', 'N/A')}",
            "52 Week Low": f"${info.get('fiftyTwoWeekLow', 'N/A')}",
            "Dividend Yield": f"{info.get('dividendYield', 'N/A') * 100 if info.get('dividendYield') else 'N/A'}%",
        }

        for key, value in metrics.items():
                st.write(f"**{key}:** {value}")

# st.write(info)

# Load data
dataLoadState = st.sidebar.text("📥 Loading data...")
data = load_data(selectedStock)
if data.empty:
    st.stop()
dataLoadState.markdown(":white_check_mark: Data loaded successfully!")

col1, col2 = st.columns(2)

with col1:
    # Display raw data
    st.subheader(f"🗃️ Raw Data for {selectedStock}")
    st.write(data.head(11))
with col2:
    st.subheader(f"Financials Data for {selectedStock}")
    st.write(load_financials(selectedStock))

# st.subheader(f"Calls {selectedStock}")
# st.write(load_calls(selectedStock))

currentPrice = data['Close'].iloc[-1]
previousPrice = data['Close'].iloc[-2]
priceChange = currentPrice - previousPrice
priceChangePCT = (priceChange / (previousPrice + currentPrice)) * 100

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label= "Current Price ($)", 
              value = f"$ {currentPrice:.2f}")
with col2:
    st.metric(label= "Change ($)", 
              value=f"$ {priceChange:.2f}", 
              delta=f"{priceChangePCT:.2f}%")
with col3:
     st.metric(label= "Volume",
               value= f"{data['Volume'].iloc[-1]:,}")
with col4:
     st.metric(label= "Market Cap",
               value= f"$ {info.get('marketCap','N/A'):,}")

# Inforation of instutional Holders
if st.sidebar.checkbox('Show Instutional Holders'):
    st.subheader(f"Instutional Holders {selectedStock}")
    st.write(load_institutional_holders(selectedStock))

# Ensure the 'Date' column is in datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Control to display raw price chart
if st.sidebar.checkbox("Show Stock Price Chart"):
    st.subheader("📊 Stock Price Chart")
    
    # Prepare data for Altair
    open_close_data = data.melt('Date', value_vars=['Open', 'Close'], var_name='Type', value_name='Price')
    
    # Create chart with Altair
    chart = alt.Chart(open_close_data).mark_line().encode(
        x='Date:T',
        y='Price:Q',
        color='Type:N'
    ).properties(
        title=f"📈 {selectedStock} Stock Prices from {start} to {end}",
        width=800,
        height=400
    ).interactive()  # Add interactivity
    
    st.altair_chart(chart, use_container_width=True)

# Prepare data for Prophet
df_train = data[['Date', 'Close']].rename(columns={"Date": 'ds', "Close": "y"})

# Initialize and fit Prophet model
m = Prophet()
m.fit(df_train)

# Create dataframe for future prediction
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)


# Control to display prediction data
if st.sidebar.checkbox("Show Prediction Data"):
    st.subheader("🔮 Prediction Data")
    st.write(forecast.tail())

# Control to display prediction chart
if st.sidebar.checkbox("Show Prediction Chart"):
    st.subheader("📈 Prediction Chart")
    
    # Create prediction chart with Altair
    forecast_plot = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    forecast_plot = forecast_plot.rename(columns={'ds': 'Date'})
    
    base = alt.Chart(forecast_plot).encode(x='Date:T')
    
    line = base.mark_line(color='blue').encode(y='yhat:Q').properties(title="📈 Stock Price Prediction")
    lower = base.mark_area(opacity=0.3, color='lightblue').encode(y='yhat_lower:Q', y2='yhat_upper:Q')
    
    chart_pred = (lower + line).interactive()
    
    st.altair_chart(chart_pred, use_container_width=True)

# Control to display prediction components
if st.sidebar.checkbox("Show Prediction Components"):
    st.subheader("📊 Prediction Components")
    fig_components = m.plot_components(forecast)
    st.pyplot(fig_components)
