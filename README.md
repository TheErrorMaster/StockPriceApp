# Stock Price App
# Author: Mauricio Macias (TheErroMaster)


## 0 Installation
Before running anything make sure you have installed Python first. <br/>
Check verions to make sure you have Python 3 downloaded. <br/>
`python3 --version`
Then you will need to create a virtual env:<br/>
`virtualenv env`<br/>
`source env/bin/activate`<br/>
And as well need to install these python modules. <br/>
- `pip install pandas` 
- `pip install streamlit`
- `pip install yfinance`

Run the project with: <br/>

`streamlit run main.py`

Then to leave the virutal env: <br/>
`deactivate`

## 1 Background 

For this project I build a simple stock price app where I can look over a stock closing price and volume. 
I first fetch the data online to get the list S&P 500 companies.
Then made a dropdown to choose a S&P 500 company so I could show its everyday closing price and volume.

## 2 Demostration

![](app.png)