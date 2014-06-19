#!/usr/local/bin/python3

import input, re

years = set()

keywords = []; patterns = []; results = {}

for keyword in open('keywords.txt','r'):
  patterns.append(re.compile(keyword.rstrip(),re.IGNORECASE))
  results[patterns[-1].pattern] = {}


l = input.anzns('anzns.txt')

#l += input.factiva('factiva.txt')]


for tuple in l:
  for pattern in patterns:
    years.add(tuple[0])
    try:
      results[pattern.pattern][tuple[0]] += len(pattern.findall(tuple[1]))
    except:
      results[pattern.pattern][tuple[0]] = len(pattern.findall(tuple[1]))


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
