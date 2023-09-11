from pathlib import Path
import pandas as pd

input_datapath = Path(__file__) / ".." / ".." / ".." / "data" / "movies.csv"
output_datapath = Path(__file__) / ".." / ".." / ".." / "data" / "movies_combined.csv"

print( "input path:", input_datapath.resolve() )
print( "output path:", output_datapath.resolve() )

# columns of interest for this experiment
columns = [
    "title",
    "release_date",
    "genres",
    "original_language",
    "vote_average",
    "overview",
    # "runtime",
    "tagline",
]

# How would like to combine the columns?
def combine_columns(row):
    return row["title"].strip() + " " + row["overview"].strip() + " " + row["tagline"].strip()

df = pd.read_csv(input_datapath.resolve(), index_col=0)
df = df[columns]
df = df.dropna()

df["combined"] = df.apply(combine_columns, axis=1)

df.to_csv(output_datapath.resolve())