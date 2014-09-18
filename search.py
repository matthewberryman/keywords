#!/usr/local/bin/python3

import input, re

from textblob import TextBlob

years = set()

keywords = []; patterns = []; results = {}; sentiment = {}
positive_words = set(); negative_words = set(); negation_words = set()

for keyword in open('keywords.txt','r'):
  patterns.append(re.compile(keyword.rstrip(),re.IGNORECASE))
  results[patterns[-1].pattern] = {}

for positive_word in open('positive_words.txt','r'):
  positive_words.add(positive_word.rstrip())

for negative_word in open('positive_words.txt','r'):
  negative_words.add(negative_word.rstrip())

for negation_word in open('positive_words.txt','r'):
  negation_words.add(negation_word.rstrip())


print(positive_words)

l = input.anzns('anzns.txt')

#l += input.factiva('factiva.txt')]

words = re.compile('\w+')

sentiment = {'local': 0, 'other': 0}
n = {'local': 0, 'other': 0}


for tuple in l:
  for pattern in patterns:
    years.add(tuple[0])
    try:
      results[pattern.pattern][tuple[0]] += len(pattern.findall(tuple[2]))
    except:
      results[pattern.pattern][tuple[0]] = len(pattern.findall(tuple[2]))

  # Sentiment analysis:
  blob = TextBlob(tuple[2])
  polarity = blob.sentiment.polarity
  if (tuple[1].startswith('Wollongong') or tuple[1].startswith('Kiama')):
    sentiment['local'] += blob.sentiment.polarity
    n['local'] += 1
  else:
    sentiment['other'] += blob.sentiment.polarity
    n['other'] += 1

for key in sentiment.keys():
  sentiment[key] = sentiment[key]/n[key]

print(sentiment)

print('',end=',')

years = list(years)
years.sort()

for year in years:
    print(year,end=',')

print()


for pattern in patterns:
    print(pattern.pattern,end=',')
    for year in years:
      print(results[pattern.pattern][year],end=',')
    print()

print()

print()

for location in sentiment:
  print(location+','+str(sentiment[location]))
