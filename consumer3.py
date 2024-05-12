from kafka import KafkaConsumer
from pymongo import MongoClient
from collections import Counter
import matplotlib.pyplot as plt

# MongoDB Settings
mongo_host = 'localhost'
mongo_port = 27017
mongo_db_name = 'streaming_database'
mongo_collection_name = 'insightful_results'

# Establish MongoDB Connection
def connect_to_mongodb():
    client = MongoClient(mongo_host, mongo_port)
    db = client[mongo_db_name]
    collection = db[mongo_collection_name]
    return collection

# Save Data to MongoDB
def save_data_to_mongodb(collection, data):
    collection.insert_one(data)

# Analyze Data and Visualize Insights
def advanced_analysis(consumer, topic):
    collection = connect_to_mongodb()
    frequent_items = Counter()
    total_transactions = 0
    
    for message in consumer:
        transaction = message.value.decode('utf-8').split(',')
        
        # Perform unique analysis: Count occurrences of each item in real-time
        frequent_items.update(transaction)
        total_transactions += 1
        
        # Print and visualize insights periodically
        if total_transactions % 100 == 0:
            print(f"Total transactions processed: {total_transactions}")
            print("Top 5 most frequent items:")
            for item, count in frequent_items.most_common(5):
                print(f"- {item}: {count} occurrences")
            
            # Visualize frequent item occurrences
            items, counts = zip(*frequent_items.most_common())
            plt.bar(items, counts)
            plt.xlabel('Item')
            plt.ylabel('Occurrences')
            plt.title('Frequent Item Occurrences')
            plt.xticks(rotation=45)
            plt.show()
            
            # Save insights in MongoDB
            data = {
                'total_transactions': total_transactions,
                'top_5_frequent_items': {item: count for item, count in frequent_items.most_common(5)}
            }
            save_data_to_mongodb(collection, data)

def main():
    kafka_servers = 'localhost:9092'
    topic = 'amazon_stream'
    
    consumer = KafkaConsumer(topic, bootstrap_servers=kafka_servers, group_id='group4')
    advanced_analysis(consumer, topic)

