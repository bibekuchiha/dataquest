## 1. Reading CSV Files with Encodings ##

import pandas as pd

laptops = pd.read_csv('laptops.csv', encoding = 'Latin-1')
print(laptops.info())

## 2. Cleaning Column Names ##

new_columns = []
for col in laptops.columns:
    clean_c = col.strip()
    new_columns.append(clean_c)
    
print(new_columns)

laptops.columns = new_columns

## 3. Cleaning Column Names Continued ##

import pandas as pd
laptops = pd.read_csv('laptops.csv', encoding='Latin-1')

def clean_col(col):
    col = col.strip()
    col = col.replace('Operating System','os')
    col = col.replace(' ','_')
    col = col.replace('(','')
    col = col.replace(')','')
    col = col.lower()
    
    return col

new_columns=[]
for c in laptops.columns:
    clean_c = clean_col(c)
    new_columns.append(clean_c)
    
laptops.columns = new_columns
print(laptops.columns)
    

## 4. Converting String Columns to Numeric ##

unique_ram = laptops['ram'].unique()
print(unique_ram)



## 5. Removing Non-Digit Characters ##

laptops['ram'] = laptops['ram'].str.replace('GB','')

unique_ram = laptops['ram'].unique()
print(unique_ram)

## 6. Converting Columns to Numeric Dtypes ##

laptops["ram"] = laptops["ram"].str.replace('GB','')

laptops['ram'] = laptops['ram'].astype(int)

dtypes = laptops.dtypes
print(dtypes)

## 7. Renaming Columns ##

laptops["ram"] = laptops["ram"].str.replace('GB','').astype(int)

laptops.rename({'ram':'ram_gb'},axis =1 , inplace=True)
ram_gb_desc = laptops['ram_gb'].describe()
print(ram_gb_desc)

## 8. Extracting Values from Strings ##

laptops["gpu_manufacturer"] = (laptops["gpu"]
                                       .str.split()
                                       .str[0]
                              )


laptops['cpu_manufacturer'] = (laptops['cpu'].str.split().str[0])

cpu_manufacturer_counts = laptops['cpu_manufacturer'].value_counts()
print(cpu_manufacturer_counts)

## 9. Correcting Bad Values ##

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}

laptops['os'] = laptops['os'].map(mapping_dict)
print(laptops['os'].unique())

## 10. Dropping Missing Values ##

laptops_no_null_rows = laptops.dropna()

laptops_no_null_cols = laptops.dropna(axis=1)

## 11. Filling Missing Values ##

value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()
2
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"
3
laptops.loc[laptops["os"] == "No OS", "os_version"] = "Version Unknown"
4
value_counts_after = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()

## 12. Challenge: Clean a String Column ##

laptops['weight'] = laptops['weight'].str.replace('kgs','')
laptops['weight'] = laptops['weight'].str.replace('kg','').astype(float)

laptops.rename({'weight':'weight_kg'}, axis=1, inplace=True)


laptops.to_csv('laptops_cleaned.csv',index = False)
