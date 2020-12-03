## 2. Introduction to the data ##

import pandas as pd

dc_listings = pd.read_csv('dc_airbnb.csv')
print(dc_listings.head(1))

## 4. Euclidean distance ##

import numpy as np
our_acc_value = 3

first_living_space_value = dc_listings.iloc[0]['accommodates']

first_distance = np.abs(first_living_space_value - our_acc_value)
print(first_distance)

## 5. Calculate distance for all observations ##

import numpy as np

our_listing_accomodates = 3

dc_listings['distance'] =  dc_listings['accommodates'].apply(lambda x: np.abs(x- our_listing_accomodates))

print(dc_listings['distance'].value_counts())
                                                          

## 6. Randomizing, and sorting ##

import numpy as np
np.random.seed(1)
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
dc_listings = dc_listings.sort_values('distance')
print(dc_listings.iloc[0:10]['price'])

## 7. Average price ##

import numpy as np

dc_listings['price'] = dc_listings['price'].str.replace(',','')
dc_listings['price'] = dc_listings['price'].str.replace('$','')

dc_listings['price'] = dc_listings['price'].astype(float)

mean_price = np.mean(dc_listings['price'].head())
print(mean_price)
                                                        
                                                      

## 8. Function to make predictions ##

# Brought along the changes we made to the `dc_listings` Dataframe.
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

import numpy as np

def predict_price(new_listing):
    temp_df = dc_listings.copy()
    ## Complete the function.
    temp_df['distance'] = temp_df['accommodates'].apply(lambda x: np.abs(x - new_listing))
    temp_df = temp_df.sort_values('distance')
    temp_df = np.mean(temp_df['price'].head())
    return temp_df

acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)

print(acc_one, acc_two, acc_four)