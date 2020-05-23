import pandas as pd

df = pd.read_csv("movies_only.tsv", sep="\t")
df2 = df.loc[df["startYear"] == "2020"]
df2.set_index("tconst")
df2.to_csv("sample.tsv", sep="\t")