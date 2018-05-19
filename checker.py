# Import statements
## Some are marked as not used, they are, computers know nothing.
import pandas as pd
import numpy as np
import datetime
import json
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import requests
import sys
import matplotlib.pyplot as plt
import warnings
import quandl
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, svm

warnings.simplefilter('always', DeprecationWarning)

# Input Statement #1
companyname2 = input(
    "What is the name of the company you'd like stock prices for? (Please input a NASDAQ stock, and if you get an error, break the program and try it again. ")

# Capitalises the symbol you put in above
companynameupper = companyname2.upper()


# The below code is a definition for the Yahoo Finance API which returns the company name from the symbol input
def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(
        symbol)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']


# Changes the name of the string for the stock price API call below
company = get_symbol(companynameupper)

# Clears the page and prints the company name collected from Yahoo Finance
print("")
print(companynameupper + "/" + company + " it is!")
print("")
print("We're just retrieving your data...")
print("")

# Changes the company string for the call below
companyname = companynameupper

ts = TimeSeries(key='PIUH8SB6UWPJ7Q14', output_format='pandas')
data, meta_data = ts.get_intraday(
    symbol=companyname, interval='1min', outputsize='full')

# Pretty Prints the data returned above
pprint(data.head(1))
# Queries about the stock buying bit
print("")
print("Do you want a graph? (Y/N)")
print("")

# raw_input returns the empty string for "enter"
yes = {'yes', 'y', 'ye', ''}
no = {'no', 'n'}

choice = input().lower()
if choice in yes:
    print("One graph, coming right up! (Close it to proceed)")
    print("")
    data, meta_data = ts.get_intraday(
        symbol=companyname, interval='1min', outputsize='full')
    data['4. close'].plot()
    plt.title('Stock price for ' + company + ' (1 minute period)')
    plt.show()
elif choice in no:
    print("")
    print("Okay...")
    print("")
else:
    sys.stdout.write(
        "Please try the script again, and respond with 'yes' or 'no'")

# PART 2: Prediction

print("")
choice = input("Would you like me to forecast the future of " +
               companynameupper + "/" + company + "'s share price? ").lower()
print("")
if choice in yes:
    warnings.filterwarnings("ignore")
    numberofdays = int(
        input("How many days into the future would you like to predict? "))
    df = quandl.get("WIKI/" + companynameupper)
    df = df[['Adj. Close']]

    print("")
    print("Calculating...")
    print("")

    # Forecast variables
    forecast_out = int(numberofdays)  # predicting 30 days into future
    df['Prediction'] = df[['Adj. Close']].shift(
        -forecast_out)  #  label column with data shifted

    # Axis variable assignments and training
    X = np.array(df.drop(['Prediction'], 1))
    X = preprocessing.scale(X)
    X_forecast = X[-forecast_out:]  # set X_forecast equal to last 30
    X = X[:-forecast_out]  # remove last 30 from X
    y = np.array(df['Prediction'])
    y = y[:-forecast_out]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Training
    clf = LinearRegression()
    clf.fit(X_train, y_train)

    print("")
    choice = input(
        "Would you like the raw data before you see the graph? ").lower()
    if choice in yes:
        print("Okay, here is the algorithm confidence:")
        print("")
        # Displays algorith confidence
        confidence = clf.score(X_test, y_test)
        print("confidence: ", confidence)
        print("")
        print("Here are the raw values from the algorithm:")
        forecast_prediction = clf.predict(X_forecast)
        print(forecast_prediction)
        print("")
        print("I'll just make you a graph with the predictions now.")
        print("")
        plt.plot(forecast_prediction)
        plt.ylabel('Forecast for ' + companyname2 + "'s stock price")
        plt.show()
    elif choice in no:
        print("")
        print("Okay, see you next time :)")
        forecast_prediction = clf.predict(X_forecast)
        print("")
        plt.plot(forecast_prediction)
        plt.ylabel('Prediction for ' + companynameupper + "/" + company +
                   "'s stock price")
        plt.show()
    else:
        sys.stdout.write(
            "Please start the script again, and respond with 'yes' or 'no'")
elif choice in no:
    print("")
    print("Okay, goodbye!")
else:
    sys.stdout.write(
        "Please start the script again, and respond with 'yes' or 'no'")
