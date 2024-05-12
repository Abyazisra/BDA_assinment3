from kafka import KafkaConsumer
from pymongo import MongoClient
from collections import Counter
import itertools

# MongoDB Connection Configuration
mongo_host = 'localhost'
mongo_port = 27017
mongo_db_name = 'streaming_data_db'
mongo_collection_name = 'apriori_results'

# Establish MongoDB Connection
def connect_to_mongodb():
    client = MongoClient(mongo_host, mongo_port)
    db = client[mongo_db_name]
    collection = db[mongo_collection_name]
    return collection

# Store Frequent Itemsets in MongoDB
def store_frequent_itemsets_in_mongodb(collection, frequent_itemsets):
    data = {'frequent_itemsets': frequent_itemsets}
    collection.insert_one(data)

# Implement Apriori Algorithm to Find Frequent Itemsets
def apriori_algorithm(transactions, min_support):
    item_counts = Counter()
    frequent_itemsets = []
    
    # Count occurrences of items
    for transaction in transactions:
        item_counts.update(transaction)
    
    # Generate frequent itemsets
    for item, count in item_counts.items():
        if count >= min_support:
            frequent_itemsets.append({item})
    
    k = 2
    while True:
        candidates = set()
        for itemset1, itemset2 in itertools.combinations(frequent_itemsets, 2):
            union_itemset = itemset1.union(itemset2)
            if len(union_itemset) == k:
                candidates.add(union_itemset)
        
        if not candidates:
            break
        
        # Count occurrences of candidate itemsets
        candidate_counts = Counter()
        for transaction in transactions:
            for candidate in candidates:
                if candidate.issubset(transaction):
                    candidate_counts[candidate] += 1
        
        # Prune candidate itemsets that do not meet minimum support
        frequent_itemsets = [itemset for itemset, count in candidate_counts.items() if count >= min_support]
        if not frequent_itemsets:
            break
        
        k += 1
    
    return frequent_itemsets

# Consume Data and Apply Apriori Algorithm
def consume_data_and_apply_apriori(consumer, topic, min_support):
    collection = connect_to_mongodb()
    transactions = []
    for message in consumer:
        transaction = message.value.decode('utf-8').split(',')
        transactions.append(transaction)
        
        # Apply Apriori algorithm to find frequent itemsets
        frequent_itemsets = apriori_algorithm(transactions, min_support)
        
        # Store frequent itemsets in MongoDB
        store_frequent_itemsets_in_mongodb(collection, frequent_itemsets)

# Main Function
def main():
    bootstrap_servers = 'localhost:9092'
    topic = 'amazon_data'
    min_support = 2  # Minimum support threshold for Apriori algorithm
    
    consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers, group_id='group1')
    consume_data_and_apply_apriori(consumer, topic, min_support)

if __name__ == "__main__":
    main()
