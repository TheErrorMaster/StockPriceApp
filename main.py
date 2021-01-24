import yfinance as yf
import streamlit as st
import pandas as pd 


st.title("Stock Price App")
st.header("List of the S&P 500")

@st.cache() # use cache to load faster
def load_data():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    df = pd.read_html(url,header = 0) # fetch data here
    df = df[0] # first Dataframe
    # clean data
    df['Founded'] = df['Founded'].str.extract(r'^(\d{4})', expand=False) # clean data get only first date
    # df = df.sort_values(['Founded'], ascending=[0]) # sort by founded and by ascending order
    df = df.drop(['SEC filings','CIK'],axis=1) # drop two column unnecessary columns
    df['Date first added'] = df['Date first added'].fillna(df['Founded']) # nan to founded
    return df

df = load_data()
st.write(df)


option = st.sidebar.selectbox('Choose Company', df['Symbol'])
# st.sidebar.write('you selected:', option)

optionName = df.loc[df['Symbol'] == option]
optionName = optionName['Security'].to_string(index=0)
st.write("Stocked Picked: " ,optionName)



#define the ticker symbol
#get data on this ticker
tickerData = yf.Ticker(option)

# Major holders
st.subheader("Stock Major Holders")
st.write(tickerData.major_holders)

#get the historical prices for this ticker
starts = df.loc[df['Symbol'] == option]
starts = pd.to_datetime(starts['Date first added'],format="%Y-%m-%d").to_string(index=0)
ends = pd.Timestamp("today").strftime("%Y-%m-%d")
tickerDf = tickerData.history(period='1d', start=starts, end=ends)

st.header("Stock Closing Price")

st.line_chart(tickerDf.Close)

st.header("Stock Volume")

st.line_chart(tickerDf.Volume)
