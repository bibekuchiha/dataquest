## 1. Introduction ##

import pandas as pd

hn =pd.read_csv('hacker_news.csv')
print(hn.head())

## 2. The Regular Expression Module ##

import re

titles = hn["title"].tolist()

python_mentions = 0

pattern = "[Pp]ython"

for t in titles:
    if re.search(pattern, t):
        python_mentions +=1
        
print(python_mentions)

## 3. Counting Matches with pandas Methods ##

pattern = '[Pp]ython'

titles = pd.Series(hn['title'])
print(titles)

python_mentions = titles.str.contains(pattern).sum()
print(python_mentions)

## 4. Using Regular Expressions to Select Data ##

titles = hn['title']

ruby_titles = titles[titles.str.contains("[Rr]uby")]
print(ruby_titles)

## 5. Quantifiers ##

# The `titles` variable is available from
# the previous screens

email_bool = titles.str.contains("e-?mail")
email_count = email_bool.sum()
print(email_count)

email_titles = titles[email_bool]
print(email_titles)

## 6. Character Classes ##

pattern = "\[\w+\]"

tag_titles = titles.str.contains(pattern)

tag = titles[tag_titles]
print(tag)
tag_count = tag_titles.sum()
print(tag_count)

## 7. Accessing the Matching Text with Capture Groups ##

pattern = r"\[(\w+)\]"

tag_freq = titles.str.extract(pattern).value_counts()
print(tag_freq)

## 8. Negative Character Classes ##

def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches.head(10)
    return first_10

pattern = r"[jJ]ava[^sS]"
java_titles = titles[titles.str.contains(pattern)]
print(java_titles)

## 9. Word Boundaries ##

pattern = r"\b[jJ]ava\b"

java_titles = titles[titles.str.contains(pattern)]

print(java_titles)

## 10. Matching at the Start and End of Strings ##

pattern_beginning = r"^\[\w+\]"
beginning_count = titles.str.contains(pattern_beginning).sum()
print(beginning_count)

pattern_ending = r"\[\w+\]$"

ending_count = titles.str.contains(pattern_ending).sum()

print(ending_count)



## 11. Challenge: Using Flags to Modify Regex Patterns ##

import re

email_tests = pd.Series(['email', 'Email', 'e Mail', 'e mail', 'E-mail',
              'e-mail', 'eMail', 'E-Mail', 'EMAIL', 'emails', 'Emails',
              'E-Mails'])

email_mentions = titles.str.contains(r"\be[\-\s]?mails?\b", flags=re.I).sum()

print(email_mentions)