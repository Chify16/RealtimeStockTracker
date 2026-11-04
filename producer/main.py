import time

from producer_setup import init_producer, topic


from extract import connect_to_api, extract_jason # import the functions from the extract.py file

def main(): # define the main function to run the program
    
    producer = init_producer() # call the init_producer function to initialize the Kafka producer
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
        
        producer.send(topic, result)
        print(f"Data sent to topic {topic} topic") # print the data sent to the Kafka topic for debugging purposes
        time.sleep(2)  # Add a delay of 2 second between sending messages to avoid overwhelming the Kafka broker
        
    producer.flush()  # Ensure all messages are sent before closing the producer
    producer.close()  # Close the Kafka producer after sending all messages
    
    return None # return the extracted records for further processing

if __name__ == "__main__":
    main()  
    
    