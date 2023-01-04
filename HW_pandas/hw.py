import pandas as pd

path_in = "data/iris.csv"
path_out = "data/iris_out.xlsx"
data = pd.read_csv(path_in, encoding = 'utf-8')
data.to_excel(path_out)