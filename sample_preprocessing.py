import json
import pandas as pd
import time
from tqdm import tqdm
from kafka import KafkaProducer

class DataSampler:
    def __init__(self, input_file, output_file, target_size_gb, filter_key='also_buy'):
        self.input_file = input_file
        self.output_file = output_file
        self.target_size_bytes = target_size_gb * 1024**3
        self.filter_key = filter_key

    def sample_data(self):
        current_size_bytes = 0
        with open(self.input_file, 'r', encoding='utf-8') as infile, open(self.output_file, 'w', encoding='utf-8') as outfile:
            for line in tqdm(infile):
                record = json.loads(line)
                if record.get(self.filter_key):
                    outfile.write(json.dumps(record) + '\n')
                    current_size_bytes += len(line.encode('utf-8'))
                if current_size_bytes >= self.target_size_bytes:
                    break
        print(f"Sampling completed. Output size: {current_size_bytes/ 1024**3:.2f} GB")

class DataProcessor:
    def __init__(self, input_file, output_file, interval=60):
        self.input_file = input_file
        self.output_file = output_file
        self.interval = interval

    def preprocess_real_time(self):
        while True:
            sampled_data = self.load_dataset()
            preprocessed_data = self.preprocess_data(sampled_data)
            self.save_preprocessed_data(preprocessed_data)
            time.sleep(self.interval)

    def load_dataset(self):
        sampled_data = pd.read_json(self.input_file, lines=True)
        return sampled_data

    def preprocess_data(self, data):
        data = data.drop_duplicates()
        data = data.dropna()
        return data

    def save_preprocessed_data(self, data):
        data.to_json(self.output_file, orient='records', lines=True)
        print(f"Preprocessed data saved to: {self.output_file}")

def main():
    input_file = 'sampled_amazon_dataset.json'
    output_file = 'preprocessed_amazon_dataset.json'
    target_size_gb = 15
    
    data_sampler = DataSampler(input_file, output_file, target_size_gb)
    data_sampler.sample_data()

    data_processor = DataProcessor(input_file, output_file)
    data_processor.preprocess_real_time()

if __name__ == "__main__":
    main()
