from kafka import KafkaProducer
import json
import time

class DataStreamer:
    def __init__(self, server, file, topic):
        self.server = server
        self.file = file
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.server)
    
    def stream_data(self):
        with open(self.file, 'r') as f:
            for line in f:
                data = json.loads(line)
                self.producer.send(self.topic, json.dumps(data).encode('utf-8'))
                
              # Simulating real-time streaming
                time.sleep(1)  
            self.producer.flush()

def main():
    kafka_server = 'localhost:9092'
    input_file = 'preprocessed_amazon_dataset.json'
    kafka_topic = 'amazon_data'
    
    data_streamer = DataStreamer(server=kafka_server, file=input_file, topic=kafka_topic)
    data_streamer.stream_data()

if __name__ == "__main__":
    main()
