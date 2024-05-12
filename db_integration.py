from kafka import KafkaConsumer
from pymongo import MongoClient

# MongoDB Configuration
mongo_host = 'localhost'
mongo_port = 27017
mongo_db_name = 'streaming_data_db'
mongo_collection_name = 'frequent_itemsets'

# Function to connect to MongoDB
def connect_to_mongodb():
    client = MongoClient(mongo_host, mongo_port)
    db = client[mongo_db_name]
    collection = db[mongo_collection_name]
    return collection

# Function to store data in MongoDB
def store_data_in_mongodb(collection, data):
    collection.insert_one(data)

# Function to consume data and store frequent itemsets in MongoDB
def consume_data_and_store_results(consumer, topic):
    collection = connect_to_mongodb()
    for message in consumer:
        data = {'frequent_itemsets': message.value.decode('utf-8')}
        store_data_in_mongodb(collection, data)

def main():
    bootstrap_servers = 'localhost:9092'
    topic = 'amazon_data'
    
    consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers, group_id='group1')
    consume_data_and_store_results(consumer, topic)

if __name__ == "__main__":
    main()
