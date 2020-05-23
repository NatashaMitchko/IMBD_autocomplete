import pandas as pd
import pickle
from time import perf_counter as pc

filename = "tsv/sample.tsv"
print(f"generating LUT for {filename}")

df = pd.read_csv(
    filename,
    sep="\t",
    usecols=["tconst", "primaryTitle", "startYear"],
)

t0 = pc()
result = {}
for _, row in df.iterrows():
    title = row["primaryTitle"]
    year = row["startYear"]
    result[row["tconst"]] = f"{title} ({year})"
t1 = pc()
print(f"Create time: {t1-t0}")

filename = "IMBD_lookup.pkl"
print(f"saving to {filename}")
with open(filename, "wb") as f:
    pickle.dump(result, f)
print("saved")
