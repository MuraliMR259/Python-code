import pandas as pd

data = pd.read_excel (r'join.xlsx')
df = pd.DataFrame(data, columns= ['join_type','join_condition','join_dimensions_or_fact'])


def sample():
    print(df.columns)
sample()