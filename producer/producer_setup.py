from kafka import KafkaProducer
import json

topic = 'stock_analysis'  # Define the topic name for the Kafka producer

def init_producer():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9094',  # Specify the Kafka broker address 
        value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize the data to JSON format
    )
    return producer