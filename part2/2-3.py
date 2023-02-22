import pandas as pd

file_path = "./read_json_sample.json"
df = pd.read_json(file_path)

print(df)
