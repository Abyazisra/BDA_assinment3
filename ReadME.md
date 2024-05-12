# Real-Time Data Analysis with Kafka and MongoDB

## Project Overview


This project exemplifies real-time data analysis using Apache Kafka for message streaming and MongoDB for result storage. The primary focus is on frequent itemset mining of Amazon metadata within a streaming framework.

## Methodology

1. **Dataset Sampling**: Initially, the dataset is sampled to a manageable size (15 GB) using a customized Python script. This sampled dataset serves as the foundation for subsequent analyses.

2. **Data Preprocessing**: The sampled dataset undergoes preprocessing to cleanse and format it for analysis. Duplicate records are eliminated, and missing values are addressed.

3. **Dynamic Preprocessing**: A real-time preprocessing mechanism is devised to continually load the sampled dataset, preprocess it, and persist the preprocessed data to a JSON file at regular intervals. This ensures data currency and analysis readiness.

4. **Setting up the Streaming Pipeline**: A Kafka producer application is engineered to stream the preprocessed data in real-time. Three consumer applications are created to subscribe to the producer's data stream.

## Frequent Itemset Mining

In this project context, frequent itemset mining entails identifying sets of items that frequently co-occur in the dataset. This is crucial in various data-driven applications such as market basket analysis and recommendation systems.

### Consumer Applications:

1. **Consumer 1 (Apriori Algorithm)**: Implements the Apriori algorithm, a seminal technique for mining frequent itemsets. The algorithm employs a bottom-up strategy to generate candidate itemsets and prune infrequent ones based on the downward closure property.

2. **Consumer 2 (PCY Algorithm)**: Adopts the PCY (Park-Chen-Yu) algorithm, an enhancement over Apriori, leveraging hash-based techniques to reduce the number of candidate itemsets. It utilizes a hash table to count item pairs and filters out infrequent pairs before generating candidates, thereby reducing memory overhead.

3. **Consumer 3 (Innovative Approach)**: Takes a unique stance towards frequent itemset mining by exploring bespoke algorithms, optimization techniques, and real-time insights and visualizations tailored to streaming data characteristics. This approach focuses on creativity and adaptability to derive meaningful patterns in real-time.

## Database Integration

Each consumer is configured to interface with MongoDB for result storage. MongoDB's non-relational nature aligns with the schema-less structure of streaming data, offering flexibility in data modeling and scalability for large-scale data handling.

## Why MongoDB?

MongoDB is selected for its non-relational architecture, which complements the schema-less nature of streaming data. It offers flexibility in data modeling and scalability, making it well-suited for storing streaming data analysis results.

## Dependencies

- Python 3.x
- Kafka (for message streaming)
- MongoDB (for result storage)
- Required Python libraries (kafka-python, pandas, tqdm, pymongo, matplotlib)

## Usage

1. Install the necessary dependencies.
2. Configure Kafka and MongoDB according to your environment.
3. Execute the sampling script to extract a dataset sample.
4. Preprocess the sampled data using the provided scripts.
5. Run the Kafka producer and consumer applications.
6. Monitor MongoDB collections for storing analysis results.

## Contributors

- Abyaz Israr 22i-2056
- Sarmad Ali 22i-1997
- Saim Mukhtar 22-1415

