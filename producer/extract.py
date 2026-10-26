import requests
from config import logger, url, headers
from dotenv import load_dotenv #for loading environment variables from .env file
load_dotenv() # Import the API key from the config module

def connect_to_api():
    
    stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]  # List of stock symbols to fetch data for
    json_response = []  # List to store the JSON data for each stock

    for stock in range(0, len(stocks)): # Loop through the list of stocks and fetch data for each stock
        querystring = {
            "symbol": f"{stocks[stock]}",# get the stock symbol from the list
            "function": "TIME_SERIES_INTRADAY", #get the function to fetch intraday data what 
            "outputsize": "compact",
            "interval": "5min",  # Set the interval to 5 minutes
            "datatype": "json", # define the datatype to be json
             "api_key": "API_KEY"  # Include the API key in the query parameters
        }  # Create query parameters for the API request

# 
        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            data = response.json()  # Store the JSON data in the dictionary
            logger.info(f"Successfully fetched data for {stocks[stock]}")  # Log a success message
            json_response.append(data) # add the data to the json_response dictionary

            print(response.json())  # Print the JSON response for debugging purposes
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching data for {stock}: {e}")
            break  # Exit the loop if there's an error to avoid further API calls
    return json_response  # Return the JSON response after fetching data for all stocks

def extract_jason(response):
    records = []
    
    for data in response:
        
        symbol = data['Meta Data']['2. Symbol']  # Access the "meta data" key in the JSON response
        
        for date_str, metrics in data['Time Series (5min)'].items():  # Loop through the "Time Series (5min)" data and extract the timestamp and values
            record = {
                "symbol": symbol,
                "date": date_str,
                "open": metrics["1. open"],
                "high": metrics["2. high"],
                "low": metrics["3. low"],
                "close": metrics["4. close"]
            }
            records.append(record)
    return records
