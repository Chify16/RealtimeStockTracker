

from extract import connect_to_api, extract_jason # import the functions from the extract.py file

def main(): # define the main function to run the program
    
    response = connect_to_api() # call the connect_to_api function to fetch data from the API
    print("Response:", response)
    print("Type:", type(response))
    
    data = extract_jason(response) # call the extract_jason function to extract data from the JSON response
    
    # specify the actual response from the extract jason function
    for stock in data:
        result = {
            
            "symbol": stock["symbol"],
            "date": stock["date"],
            "open": stock["open"],
            "high": stock["high"],
            "low": stock["low"],
            "close": stock["close"]
       
        }
        
        print(result) # print the extracted records for debugging purposes
    
    return None # return the extracted records for further processing

if __name__ == "__main__":
    main()  
    
    