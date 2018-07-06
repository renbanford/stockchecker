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
from appJar import gui

# Warning filter
warnings.simplefilter('always', DeprecationWarning)



# Creates GUI
app = gui()

app.showSplash("Stockchecker (Maintained)", fill='RosyBrown', stripe='black', fg='white', font=44)
# Add & configure widgets

app.infoBox("Tip", "Please input a NASDAQ stock, and if you get an error, break the program and try it again.", parent=None)

app.addLabel("title", "Welcome to Stockchecker (Maintained, GUI)")
app.setLabelBg("title", "RosyBrown")
app.addLabelEntry("Stock Symbol")

def press(button):
    if button == "Exit":
        app.stop()
    if button == "Predict":
            companyname2 = app.getEntry("Stock Symbol")
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
            app.infoBox(companynameupper, companynameupper + "/" + company + " it is!" " (please close this info box and wait...)", parent=None)
            print("")
            print("Retrieving data!")
            companyname = companynameupper
            numberofdays = app.integerBox("Prediction", "Please input the number of days into the future you would like to forecast.", parent=None)
            app.infoBox(companynameupper, "Please wait, depending on the amount of days you just entered, and how powerful your computer is, this could take a while... (Press ok now)")
            warnings.filterwarnings("ignore")
            df = quandl.get("WIKI/" + companynameupper)
            df = df[['Adj. Close']]

            print("")
            print("Calculating...")
            print("")

                # Forecast variables
            forecast_out = int(numberofdays)  # predicting x days into future
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


            print("Algorithm confidence:")
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
            print("")

    else:
        companyname2 = app.getEntry("Stock Symbol")
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
        app.infoBox(companynameupper, companynameupper + "/" + company + " it is!" " (please close this info box and wait...)", parent=None)
        print("")
        print("Retrieving data!")
        print("")

        # Changes the company string for the call below
        companyname = companynameupper

        ts = TimeSeries(key='PIUH8SB6UWPJ7Q14', output_format='pandas')
        data, meta_data = ts.get_intraday(
            symbol=companyname, interval='1min', outputsize='full')

        # Pretty Prints the data returned above
        pprint(data.head(1))

        print("")
        print("Making a graph")
        print("")
        app.infoBox("Graph", "Please close the graph and the main window to proceed to prediction (press ok to continue).", parent=None)
        data, meta_data = ts.get_intraday(
        symbol=companyname, interval='1min', outputsize='full')
        data['4. close'].plot()
        plt.title('Stock price for ' + company + ' (1 minute period)')
        plt.show()


# Link the buttons to the function called press
app.addButtons(["Current", "Exit", "Predict"], press)
app.setFocus("Stock Symbol")

app.go()
