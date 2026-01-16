import pandas as pd

# file PKL 
file_path = "news_human_generated.pkl"
df = pd.read_pickle(file_path)

# simpan ke CSV
df.to_csv("output_csv.csv", index=False)

print("✅ Dataset berhasil disimpan jadi Excel & CSV!")
