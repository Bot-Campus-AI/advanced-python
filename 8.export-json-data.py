import pandas as pd

# Reading a JSON file
data_frame = pd.read_json('example.json')
print("DataFrame from JSON:\n", data_frame)

# Writing to a JSON file
data_frame.to_json('output.json', orient='records', lines=True)
print("Data written to output.json")
