import pandas as pd


df =pd.read_csv('data/french_words.csv')
df_dict = df.to_dict(orient="records")
print(df_dict)
