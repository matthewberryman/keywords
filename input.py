#!/usr/local/bin/python3


def anzns(filename):
  print(filename)
  storing = False
  fulltext = ''
  store = []
  g = open(filename,'r')
  print(g)
  for line in g:
    print(line)
    if line.startswith('Full text:'):
      storing = True
      fulltext = line[10:].lower()
    else:
      if storing:
        fulltext += line

    if line.startswith('Subject:'):
      storing = False
      fulltext = ''

    if line.startswith('Publication year:'):
      year = line[18:]
      store.append((year,fulltext))

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
