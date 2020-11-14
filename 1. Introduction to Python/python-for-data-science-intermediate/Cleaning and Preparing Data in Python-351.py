## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

num_rows = len(moma)
print(num_rows)

## 2. Reading our MoMA Data Set ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Write your code here

opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"

age2 = age1.replace('one','two')
print(age2)

## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again
for row in moma:
    nationality = row[2]
    nationality = nationality.replace('(','')
    nationality = nationality.replace(')','')
    row[2] = nationality
    
print(moma[300][2])
print(moma[400][2])
print(moma[500][2])
for row in moma:
    gender = row[5]
    gender = gender.replace('(','')
    gender = gender.replace(')','')
    row[5] = gender
    
print(moma[300][5])
print(moma[400][5])
print(moma[500][5])
    

## 5. String Capitalization ##

for row in moma:
    gender = row[5]
    gender = gender.title()
    
    if not gender:
        gender = 'Gender Unknown/Other'
    row[5]=gender
    
    
    nationality = row[2]
    nationality = nationality.title()
    if not nationality:
        nationality = 'Nationality Unknown'
    row[2] = nationality

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for row in moma:
    begindate = row[3]
    enddate = row[4]
    begindate = clean_and_convert(begindate)
    enddate = clean_and_convert(enddate)
    row[3] = begindate
    row[4] = enddate

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,'')
    return string

stripped_test_data = []
for d in test_data:
    date = strip_characters(d)
    stripped_test_data.append(date)

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(date):
    if "-" in date:
        split_date = date.split("-")
        date_one = split_date[0]
        date_two = split_date[1]       
        date = (int(date_one) + int(date_two)) / 2
        date = round(date)
    else:
        date = int(date)
    return date

processed_test_data = []
for data in stripped_test_data:
    date = process_date(data)
    processed_test_data.append(date)
    

for row in moma:
    date = row[6]
    date = strip_characters(date)
    date = process_date(date)
    row[6] = date