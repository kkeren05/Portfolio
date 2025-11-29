import pandas as pd

df = pd.read_csv("archive/movies_metadata.csv", low_memory=False)
# 'title' and 'overview' are the columns we want; drop rows with no title
df = df[['title', 'overview']].dropna(subset=['title'])
# replace missing overviews with empty string
df['overview'] = df['overview'].fillna('')
# save a smaller CSV
df.to_csv("movies_small.csv", index=False)
print("Saved movies_small.csv with", len(df), "rows")