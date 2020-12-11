## 1. Introduction ##

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

train_null_counts = train.isnull().sum()
print(train_null_counts)

df_no_mv = train[train_null_counts[train_null_counts ==0].index]
print(df_no_mv.isnull().sum())

## 2. Categorical Features ##

text_cols = df_no_mv.select_dtypes(include=['object']).columns

for col in text_cols:
    print(col+":", len(train[col].unique()))
    
for cols in text_cols:
    train[cols] = train[cols].astype('category')
print('*'*15)
print(train['Utilities'].cat.codes.value_counts())

## 3. Dummy Coding ##

dummy_cols = pd.DataFrame()

for cols in text_cols:
    col_dummies = pd.get_dummies(train[cols])
    train = pd.concat([train, col_dummies], axis=1)
    del train[cols]

## 4. Transforming Improper Numerical Features ##

train['years_until_remod'] = train['Year Remod/Add'] - train['Year Built']

## 5. Missing Values ##

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

train_null_counts = train.isnull().sum()
print(train_null_counts)
df_missing_values = train[train_null_counts[(train_null_counts >0) & (train_null_counts < 584)].index]
print(df_missing_values.isnull().sum())
print(df_missing_values.dtypes)

## 6. Imputing Missing Values ##

float_cols = df_missing_values.select_dtypes(include=['float'])

float_cols = float_cols.fillna(float_cols.mean())
print(float_cols.isnull().sum())