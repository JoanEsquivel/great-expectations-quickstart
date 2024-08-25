import pandas as pd

# Load the CSV file from the URL
url = "https://raw.githubusercontent.com/great-expectations/gx_tutorials/main/data/yellow_tripdata_sample_2019-01.csv"
df = pd.read_csv(url)

# Count how many times the value 1 appears in the 'passenger_count' column
count = (df['passenger_count'] == 1).sum()
print("Number of occurrences of '1' in 'passenger_count':", count)