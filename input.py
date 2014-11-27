#!/usr/local/bin/python3

def load_training_data(filenames):
  training_set = []
  for filename in filenames:
    for line in open(filename,'r'):
      line = line.rstrip()
      if line.endswith(',-1'):
        training_set.append((line[0:-3],'neg'))
      elif line.endswith(',1'):
        training_set.append((line[0:-2],'pos'))
      elif line.endswith(',0'):
        training_set.append((line[0:-2],'neu'))
  return training_set

def anzns(filename):
  storing = False
  fulltext = ''
  year = ''
  location = ''
  store = []
  for line in open(filename,'r'):
    line = line.rstrip()
    if line.startswith('Full text:'):
      storing = True
      fulltext = line[10:].lower()
    else:
      if storing:
        fulltext += ' ' + line

    if line.startswith('Subject:'):
      storing = False
      fulltext = ''

    if line.startswith('Publication year:'):
      year = line[18:]

    if line.startswith('Place of publication:'):
      location = line[22:]
      if len(fulltext) > 1:
          store.append((year,location,fulltext))

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
