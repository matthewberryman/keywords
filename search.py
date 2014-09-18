#!/usr/local/bin/python3

import input, re

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

for tuple in l:
  for pattern in patterns:
    years.add(tuple[0])
    try:
      results[pattern.pattern][tuple[0]] += len(pattern.findall(tuple[2]))
    except:
      results[pattern.pattern][tuple[0]] = len(pattern.findall(tuple[2]))

  # Sentiment analysis:
  modifying = False
  negative = 0
  positive = 0
  for word in words.findall(tuple[2].lower()):
    if word in negation_words:
      modifying = True
    elif word in positive_words:
      if modifying:
        negative += 1
        modifying = False
      else:
        positive += 1
    elif word in negative_words:
      if modifying:
        positive += 1
        modifying = False
      else:
        modifying = True
    else:
      modifying = False

    # Count by location (local, other):
    try:
      sentiment[tuple[1]] += positive - negative
    except KeyError:
      sentiment[tuple[1]] = 0

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
