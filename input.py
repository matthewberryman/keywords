#!/usr/local/bin/python3

import random, itertools, sys
from textblob import TextBlob



def load_set(filenames): # for loading a test or training set
  set = []
  for filename in filenames:
    for line in open(filename,'r'):
      line = line.rstrip()
      if line.endswith(',-1'):
        set.append((line[0:-3],'neg'))
      elif line.endswith(',1'):
        set.append((line[0:-2],'pos'))
      elif line.endswith(',0'):
        set.append((line[0:-2],'neu'))
  return set


def read_anzns(filename):
  title = ''
  seen = set()
  storing = False
  fulltext = ''
  year = ''
  location = ''
  store = {}

  for line in open(filename,'r'):
    line = line.rstrip()
    if line.startswith('Full text:'):
      storing = True
      fulltext = line[10:].lower()
    else:
      if storing:
        fulltext += ' ' + line
    if line == '':
      storing = False
#    if line.startswith('Subject:') or line.startswith('Credit:'):
#      storing = False
#      fulltext = ''

    if line.startswith('Title:'):
      title = line[7:]

    if line.startswith('Publication year:'):
      year = line[18:]

    if line.startswith('Place of publication:'):
      location = line[22:]

    if len(fulltext) > 1 and not storing:
        if title not in seen:
          print(location)
          by_year = {}
          try:
            by_year = store[location]
          except KeyError:
            store[location] = {}
          try:
            by_year[year].append(fulltext)
          except KeyError:
            by_year[year] = [fulltext]
          store[location] = by_year
          fulltext = ''
        else:
          seen.add(title)
        fulltext = ''
  return store

# Next function needs further testing.
def factiva(filename):
  storing = False
  dateLineNext = False
  fulltext = ''
  year = ''
  for line in open(filename,'r'):
    if line.endswith('words'):
      dateLineNext = True
      storing = True

    if dateLineNext:
      year = line[-4:]
      dateLineNext = False;

    if storing:
      fulltext += line

    if line.startswith('Document'):
      storing = False
      store.append((year,fulltext))
      fulltext = ''

    return store

# Generate input data

if __name__ == '__main__':

  filename = ''
  if len(sys.argv) > 1:
    filename = sys.argv[1]
  else:
    filename = 'anzns.txt'
  articles = read_anzns(filename)

  wollongong_articles = []
  kiama_articles = []
  other_articles = []

  wollongong_test = open('wollongong_test.txt','w')
  wollongong_training = open('wollongong_training.txt','w')
  kiama_test = open('kiama_test.txt','w')
  kiama_training = open('kiama_training.txt','w')
  other_test = open('other_test.txt','w')
  other_training = open('other_training.txt','w')

  for location in articles.keys():
    if location.startswith('Wollongong'):
      for article in [item for sublist in articles[location].values() for item in sublist]:
        wollongong_articles.append(article)
    elif location.startswith('Kiama'):
      for article in [item for sublist in articles[location].values() for item in sublist]:
        kiama_articles.append(article)
    else:
      for article in [item for sublist in articles[location].values() for item in sublist]:
        other_articles.append(article)

  for i in range(88):
    wollongong_article = TextBlob(random.choice(wollongong_articles))
    for sentence in wollongong_article.sentences:
      if 'NBN' in sentence:
        if i < 44:
          wollongong_test.write(str(sentence) + ',\n')
        if i > 44:
          wollongong_training.write(str(sentence) + ',\n')

  for i in range(min(len(kiama_articles),88)):
    print(str(i))
    kiama_article = TextBlob(kiama_articles[i])
    for sentence in kiama_article.sentences:
      if 'NBN' in sentence:
        if i < 44:
          kiama_test.write(str(sentence) + ',\n')
        if i > 44:
          kiama_training.write(str(sentence) + ',\n')

  for i in range(min(len(other_articles),88)):
    other_article = TextBlob(random.choice(other_articles))
    for sentence in other_article.raw_sentences:
      if 'NBN' in sentence:
        if i < 44:
          other_test.write(str(sentence) + ',\n')
        if i > 44:
          other_training.write(str(sentence) + ',\n')
