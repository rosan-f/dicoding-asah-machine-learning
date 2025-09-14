import pandas as pd
from tabulate import tabulate


def split_missing_column(df, treshold = 50):
    missing_values = df.isnull().sum()
    missing_ratio = missing_values / len(df) * 100

    less = missing_values[(missing_ratio < treshold) & (missing_values > 0)].index
    over = missing_values[missing_ratio > treshold].index

    return less, over, missing_ratio, missing_values



train = pd.read_csv("dataset/train.csv")

less, over, missing_ratio, missing_values = split_missing_column(train,treshold= 50 )

# mengambil index kolom yang numerik yang missing ration nya di bawah 50%
numeric_features = train[less].select_dtypes(include="number").columns

# mengambil index kolom yang kategorikal yang missing ration nya di bawah 50%
kategorical_features =train[less].select_dtypes(include="object").columns

#mengisi nilai numerin yang NaN dengan nilai median
train[numeric_features] = train[numeric_features].fillna(train[numeric_features].median())

#mengisi nilai kategorikal yang NaN dengan nilai modus
for column in kategorical_features:
    train[column] = train[column].fillna(train[column].mode() [0])

#menghapus column yang mising ration nya di atas 50%
df = train.drop(columns=over)

#menampilkan data
describe_train = train.describe(include="all").round(2)
print(tabulate(describe_train, headers="keys", tablefmt="simple_outline"))

#cek missing values
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])



