## 1. Introduction ##

world_dev = pd.read_csv("World_dev.csv")
col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}
merged = pd.merge(left=happiness2015, right=world_dev, how='left', left_on= happiness2015['Country'], right_on=world_dev['ShortName'])

merged = merged.rename(col_renaming, axis=1)
print(merged)


## 2. Using Apply to Transform Strings ##

def extract_last_word(element):
    element = str(element)
    element = element.split()
    return element[-1]

merged['Currency Apply'] = merged['CurrencyUnit'].apply(extract_last_word)

print(merged['Currency Apply'].head())

## 3. Vectorized String Methods Overview ##

merged['Currency Vectorized'] = merged['CurrencyUnit'].str.split().str.get(-1)
print(merged['Currency Vectorized'].head())

## 4. Exploring Missing Values with Vectorized String Methods ##

lengths = merged['CurrencyUnit'].str.len()
print(lengths)

value_counts = lengths.value_counts(dropna=False)
print(value_counts)

## 5. Finding Specific Words in Strings ##

pattern = r"[Nn]ational accounts"

national_accounts = merged['SpecialNotes'].str.contains(pattern)
print(national_accounts.head())

## 6. Finding Specific Words in Strings Continued ##

pattern = r"[Nn]ational accounts"

national_accounts = merged['SpecialNotes'].str.contains(pattern, na = False)
merged_national_accounts = merged[national_accounts]

print(merged_national_accounts.head())


## 7. Extracting Substrings from a Series ##

pattern =r"([1-2][0-9]{3})"

years = merged['SpecialNotes'].str.extract(pattern)

print(years)

## 8. Extracting Substrings from a Series Continued ##

pattern = r"([1-2][0-9]{3})"

years = merged['SpecialNotes'].str.extract(pattern, expand=True)
print(years)

## 9. Extracting All Matches of a Pattern from a Series ##

pattern = r"(?P<Years>[1-2][0-9]{3})"

years = merged['IESurvey'].str.extractall(pattern)

value_counts = years['Years'].value_counts()
print(value_counts)

## 10. Extracting More Than One Group of Patterns from a Series ##

pattern = r"(?P<First_Year>[1-2][0-9]{3})/?(?P<Second_Year>[0-9]{2})?"

years = merged['IESurvey'].str.extractall(pattern)

first_two_year = years['First_Year'].str[:2]

years['Second_Year'] = first_two_year + years['Second_Year']

print(years)

## 11. Challenge: Clean a String Column, Aggregate the Data, and Plot the Results ##

merged['IncomeGroup'] = merged['IncomeGroup'].str.replace('Upper middle income','UPPER MIDDLE').str.replace('Lower middle income','LOWER MIDDLE').str.replace('High income: OECD','HIGH OECD').str.replace('Low income', 'LOW').str.replace('High income: nonOECD','HIGH NONOECD')


pv_incomes = merged.pivot_table(index = 'IncomeGroup',values='Happiness Score')
print(pv_incomes)

pv_incomes.plot(kind='bar',rot=30, ylim=(0,10))
