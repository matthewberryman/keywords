#!/usr/local/bin/python3

import random
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

    if line.startswith('Publication year:'):
      year = line[18:]

    if line.startswith('Place of publication:'):
      location = line[22:]

    if len(fulltext) > 1:
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
  return store


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
  articles = read_anzs('anzns.txt')

  # fixme: needs to be stored into arrays

  wollongong_articles = []
  kiama_articles = []
  other_articles = []



  for i in range(min(len(wollongong_articles),30)):
    wollongong_article = TextBlob(random.choice(wollongong_articles))
    wollongong_text.write('Article ' + str(i) + ':\n')
    for sentence in wollongong_article.sentences:
      if 'NBN' in sentence:
        wollongong_text.write(str(sentence) + ',\n')
    wollongong_text.write('\n')

  for i in range(min(len(kiama_articles),30)):
    kiama_article = TextBlob(kiama_articles[i])
    kiama_text.write('Article ' + str(i) + ':\n')
    for sentence in kiama_article.sentences:
      if 'NBN' in sentence:
        kiama_text.write(str(sentence) + ',\n')
    kiama_text.write('\n')

  for i in range(min(len(other_articles),30)):
    other_article = TextBlob(random.choice(other_articles))
    other_text.write('Article ' + str(i) + ':\n')
    for sentence in other_article.raw_sentences:
      if 'NBN' in sentence:
        other_text.write(str(sentence) + ',\n')
    other_text.write('\n')
