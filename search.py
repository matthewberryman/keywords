#!/usr/local/bin/python3

import input, re



keywords = []; patterns = []; results = {}

for keyword in open('keywords.txt','r'):
  patterns.append(re.compile(keyword.chomp()))
  results[keyword] = {}

print(patterns)

l = input.anzns('anzns.txt')
#l += input.factiva('factiva.txt')]

print(l)


for tuple in l:
  for pattern in patterns:
    try:
      results[pattern.pattern()][tuple[0]] += len(pattern.findall(tuple[1],re.I))
    except:
      results[pattern.pattern()][tuple[0]] = len(pattern.findall(tuple[1],re.I))

for keyword in results:
  for year, number in results[keyword].items:
    print(year,' ',keyword,' ',number)
