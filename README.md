# StockChecker

This repository contains a stock checking program built on the Alpha Vantage API for the purpose of meeting the requirements for Task 1 of the Software Design &amp; Development Preliminary Syllabus

## Introduction
StockChecker (Code developed and maintained by Benjamin Ranford, documentation in its original state created by Daniel Oroszvari) is a program developed in Python. Its purpose is that of checking the prices of company shares.

## Getting Started
1. Install dependencies
2. Download program
3. Check permissions
4. Run program



## Dependencies
#### `pandas` - An open source, BSD-licensed library built for the Python Programming Language and used to provide high-performance, simplistic data analysis tools.

#### `alpha_vantage` Application Programming Interface (API) - An API used to fetch realtime data of share prices.

#### `pprint` - A module that provides the ability to organise Python data structures into a format easily read by the user.

#### `json` - A JavaScript inspired data interchange format.

#### `matplotlib.pyplot` - A plotting library developed for the Python Programming Language and NumPy, and is used to embed plots into applications.

#### `warnings` - A module used to display alerts. Typically used to present the user with an alert on an outlier affecting the condition of the program.

#### `sys` - A module (that is always available) providing access to variables maintained by and interacting with the interpreter.

#### `requests` - An HTTP Library that allows for the sending of requests without manual labor.

#### `datetime` - This module supplies the program with a variety of date and time displays (simple and complex).

|     Feature    |  Description  |    Example   |
|----------------|---------------|--------------|
|   Ticker Symbol input from the user             |   Retrieves prices of stocks from a variety of markets             |  companyname2 = input("What is the name of the company you'd like stock prices for? Please input a NASDAQ stock, and if you get an error, break the program and try it again. ")      |
|Ticker Symbol input from the user               |Capitalises the code IF it is entered as lowercase               |companynameupper = companyname2.upper()              |
|Yahoo Finance API                 |Returns the company name from the symbol input               |"http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en"              |
|Pretty Print                 |Data produced on the program in an organised fashion               |pprint(data.head(1))              |
|Graph query     |Queries user on whether or not they would like a graph|print("") print("Do you want a graph? (Y/N)") print("")|
|Prediction of future stock prices|Produces (predicted) stock prices of the company the user selected               | input("How many days into the future would you like to predict? ")) df = quandl.get("WIKI/" + companynameupper df = df[['Adj. Close']]|

## Grok Learning Modules Used
#### Hello World!
#### Hello to you three!
#### Open Sesame!
#### Changing Text to Uppercase

## What Helped
* https://pandas.pydata.org/
* https://pypi.python.org/pypi/alpha_vantage/0.2.1
* https://docs.python.org/2/library/pprint.html
* https://docs.python.org/3/library/json.html
* https://matplotlib.org/api/pyplot_api.html
* https://docs.python.org/2/library/warnings.html
* https://docs.python.org/2/library/sys.html
* http://docs.python-requests.org/en/master/
* https://docs.python.org/2/library/datetime.html
