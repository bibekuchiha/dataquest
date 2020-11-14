## 2. Introduction to the Data ##

import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None

f500_type =  type(f500)
print(f500_type)

f500_shape = f500.shape
print(f500.shape)

print(f500)

## 3. Introducing DataFrames ##

f500_head = f500.head(6)

print(f500_head)

f500_tail = f500.tail(8)

print(f500_tail)



## 4. Introducing DataFrames Continued ##

print(f500.info())

## 5. Selecting a Column From a DataFrame by Label ##

industries = f500['industry']
print(industries)
industries_type = type(industries)
print(industries_type)

## 7. Selecting Columns From a DataFrame by Label Continued ##

countries = f500['country']

revenues_years = f500[['revenues','years_on_global_500_list']]

ceo_to_sector = f500.loc[:,'ceo':'sector']

print(countries)
print(revenues_years)
print(ceo_to_sector)

## 8. Selecting Rows From a DataFrame by Label ##

toyota = f500.loc['Toyota Motor',:]

drink_companies = f500.loc[['Anheuser-Busch InBev','Coca-Cola', 'Heineken Holding']]

middle_companies = f500.loc["Tata Motors":"Nationwide", "rank":"country"]

## 10. Value Counts Method ##

countries = f500_sel['country']
country_counts = countries.value_counts()

print(country_counts)

## 11. Selecting Items from a Series by Label ##

countries = f500['country']
countries_counts = countries.value_counts()

india = countries_counts.loc['India']

north_america = countries_counts.loc[['USA','Canada','Mexico']]
print(india)
print(north_america)
                                     
                                     

## 12. Summary Challenge ##

big_movers = f500.loc[['Aviva','HP','JD.com','BHP Billiton'],['rank','previous_rank']]

bottom_companies = f500.loc['National Grid':'AutoNation',['rank','sector','country']]

print(big_movers)
print(bottom_companies)