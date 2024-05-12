#!/bin/bash

# Function to start Kafka components

function start_kafka_components() {
    echo "Initializing Kafka components..."
    # Start Zookeeper


    zookeeper-server-start.sh config/zookeeper.properties > /dev/null 2>&1 &
    # Start Kafka server
    kafka-server-start.sh config/server.properties > /dev/null 2>&1 &
    # Add more commands to start other Kafka components if needed
}

# Function to start Kafka data producer
function start_data_producer() 
{

    echo "Starting Kafka data producer..."
    python kafka_data_producer.py > /dev/null 2>&1 &
}




# Function to start Kafka data consumers
function start_data_consumers()


 {
    echo "Starting Kafka data consumers..."
    # Start Consumer 1
    python kafka_data_consumer_1.py > /dev/null 2>&1 &
    # Start Consumer 2
    python kafka_data_consumer_2.py > /dev/null 2>&1 &
    # Start Consumer 3
    python kafka_data_consumer_3.py > /dev/null 2>&1 &
}

# Main function
function initialize_kafka() {
    start_kafka_components
    start_data_producer
    start_data_consumers
}

# Execute main function
initialize_kafka
