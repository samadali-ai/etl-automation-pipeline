# etl.py

import pandas as pd

# Step 1: Extract data
def extract(input_file):
    data = pd.read_csv(input_file)
    return data

# Step 2: Transform data (e.g., filter rows where 'value' > 20)
def transform(data):
    transformed_data = data[data['value'] > 20]
    return transformed_data

# Step 3: Load data (save to new CSV)
def load(data, output_file):
    data.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Define file paths
    input_file = '/home/abdulsamad/etl_ci/data/sample_input_data.csv'
    output_file = 'data/transformed_data.csv'
    
    # Run the ETL process
    data = extract(input_file)
    transformed_data = transform(data)
    load(transformed_data, output_file)
    print("ETL process completed and data saved to", output_file)
