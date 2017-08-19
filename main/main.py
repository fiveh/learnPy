
import pandas as pd
import sklearn.decomposition as skl

print("prog for factor analysis\n")

file_path = "../data/set2.csv"

data = pd.read_csv(file_path, encoding='cp1251', sep=';', index_col=False, na_values='?', decimal=',')
# print(data)
df = pd.DataFrame(data)
print(df)


f1 = skl.FactorAnalysis(data)
print(f1)


print("\nend")
