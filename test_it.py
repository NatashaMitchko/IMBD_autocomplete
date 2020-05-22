import pandas as pd


def show_dups(filename="movies.tsv"):
    df = pd.read_csv(filename, sep="\t")
    df_dups = df[df.duplicated(["primaryTitle"])]
    print("Duplicate Rows except last occurrence based on all columns are :")
    print(df_dups)
    return df_dups


if __name__ == "__main__":
    d = show_dups()
