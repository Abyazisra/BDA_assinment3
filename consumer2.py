from kafka import KafkaConsumer
from pymongo import MongoClient
from collections import Counter, defaultdict
import itertools

# MongoDB Configuration
mongo_host = 'localhost'
mongo_port = 27017
mongo_db_name = 'streaming_database'
mongo_collection_name = 'pcy_results'

# Connect to MongoDB
def connect_to_database():
    client = MongoClient(mongo_host, mongo_port)
    db = client[mongo_db_name]
    collection = db[mongo_collection_name]
    return collection

# Store frequent itemsets in MongoDB

def save_frequent_itemsets(collection, frequent_itemsets):
    data = {'frequent_itemsets': frequent_itemsets}
    collection.insert_one(data)




# Implement the PCY algorithm to find frequent itemsets
def pcy_algorithm(transactions, hash_table_size, min_support):
    # Initialize hash table
    hash_table = defaultdict(int)
    
    # First pass: Count item pairs and update hash table
    for transaction in transactions:
        for item1, item2 in itertools.combinations(transaction, 2):
            hash_value = (hash(item1) + hash(item2)) % hash_table_size
            hash_table[hash_value] += 1
    
    # Second pass: Filter candidate item pairs using hash table
    candidates = set()
    for item_pair, count in Counter(hash_table).items():
        if count >= min_support:
            candidates.add(item_pair)
    
    # Third pass: Count occurrences of candidate item pairs
    candidate_counts = Counter()
    for transaction in transactions:
        for candidate in candidates:
            if set(candidate).issubset(transaction):
                candidate_counts[candidate] += 1
    
    # Prune candidate item pairs
