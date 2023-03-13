import pandas as pd

# reading csv files

df1 = pd.read_csv('data/data.csv', delimiter=';')
df2 = pd.read_csv('data/iso.csv', delimiter=';')

# join csv files
inner_join = pd.merge(df1,
                      df2,
                      on='country',
                      how='inner')
inner_join.to_csv('data/result.csv', index=False)
