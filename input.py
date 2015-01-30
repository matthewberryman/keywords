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
          by_year[year].add(fulltext)
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
