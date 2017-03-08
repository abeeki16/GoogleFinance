###
### Example of reading a stock quote from Google Finance
###
### NOTE:  The Google Finance API returns a JSON object
###     which json.loads returns as a Python dict object.
###     The keys in the dict that we care about are:
###          't' - Ticker symbol
###          'l_cur' - Current price
###          'lt' - Time of last trade
###

import json        ## library to work with JavaScript Object Notation (json)
import urllib.request     ## library that allows Python to read from a web site


### This helper function takes as its input a valid stock ticker symbol
### (such as 'goog' for Google, or 'ford' for Ford Motor Company and returns
### a dict that contains the fields that the Google Finance API returns.
###
###################################################################################
###  (1) You will have to modify this code so that it does exception handling.
###      That is, if the ticker_symbol is not found, instead of the urllib.request
###      statement causing Python to halt with an error, you need to make it
###      recognize that there is an error, print an appropriate error message,
###      and return an empty dict.
###      The specific error returned by urllib.request.urlopen is:
###              urllib.error.HTTPError
###      This is the one you will need to use in your try/except statements
###################################################################################

def get_stock_quote(ticker_symbol):
    url = 'http://finance.google.com/finance/info?q='+ticker_symbol
    try:
        lines = urllib.request.urlopen(url).readlines()
    except urllib.error.HTTPError:
        print("Invalid ticker")
        return {}
    list_of_strings = []
    for line in lines:
        list_of_strings.append(line.decode('utf-8').strip('\n'))
    merged_string = ''
    for string in list_of_strings:
        if string not in ('// [', ']'):
            merged_string += string
    return json.loads(merged_string)


### Main execution thread.  Prompt the user for a stock symbol,
### use the get_stock_quote function to return a dict that has all
### the information that the Google Finance website provides, and
### print out some of the useful, interesting fields.
###
##################################################################################
###  (2) You will have to modify this code so that instead of just asking for one
###      ticker symbol, it loops through asking you for ticker symbols until you
###      enter the word quit.
###  (3) You will have to modify this code so that if you enter a ticker symbol
###      that is not found on the finance.google.com site, and your helper function
###      returns an empty dict, that you recognize that, and don't try to
###      print out the ticker symbol, current price, last trade, and full quote.
###  (4) You will need to add new code to this section that determines the highest
###      price of any of the symbols that you looked up, and prints out the ticker
###      symbol and that highest price.  HINT:  The ticker symbol can be retrieved
###      using the 't' key in the dict.  The current price can be retrieved using
###      the 'l_cur' key in the dict.  NOTE: the price in the dict is stored as
###      a string.  You will need to convert it to a float in order to see which
###      is the highest.
##################################################################################



highestStock=[{"l_cur":0}]
isSymbolValid=False
while (True):
    symbol=input("Enter a ticker symbol or type \"quit\" to end the program: ")
    
    
    if(symbol.upper()=="QUIT"):
      break

    quote=get_stock_quote(symbol)

    if (quote != {}):

        print ('\n\nticker:',quote['t'])
        print ('current price:', quote['l_cur'])
        print ('last trade:', quote['lt'])
        print ('full quote:')

        for key in quote:
          print("   ",key+":",quote[key])

        
          
        if(float(quote['l_cur'])>float(highestStock[0]["l_cur"])):
            highestStock=[quote]
        elif(float(quote["l_cur"])==float(highestStock[0]["l_cur"])):
            highestStock.append(quote)


try:
    highestStock[0]["t"]
    printHighestStocks=True
except KeyError:
    printHighestStocks=False

if (printHighestStocks):
    if (len(highestStock)==1):
        print("\n\nHighest Stock:")
    else:
        print("\n\nHighest Stocks:")
    print("\tPrice:","$"+highestStock[0]["l_cur"])

    tickerString=""
    x=0
    for stock in highestStock:
        if (x>0):
            tickerString+=", "
        tickerString+=stock["t"]
        x+=1

    if (len(highestStock)==1):
        print("\tTicker:",tickerString)
    else:
        print("\tTickers")


        
        
        

  
