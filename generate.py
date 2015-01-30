#!/usr/bin/env python3

import input
from textblob import TextBlob

# Generate some input data

l = input.read_anzns('anzns.txt')

words = re.compile('\w+')

sentiment = {'Wollongong': 0, 'Kiama': 0, 'other': 0}
n = {'Wollongong': 0, 'Kiama': 0, 'other': 0}

positive_phrases=open('positive_classifications.txt','w')
negative_phrases=open('negative_classifications.txt','w')

wollongong_text = open('wollongong.txt','w')
kiama_text = open('kiama.txt','w')
other_text = open('other.txt','w')

wollongong_articles = []
kiama_articles = []
other_articles = []

for tuple in l:

  if (tuple[1].startswith('Wollongong')):
    wollongong_articles.append(tuple[2])
  elif (tuple[1].startswith('Kiama')):
    kiama_articles.append(tuple[2])
  else:
    other_articles.append(tuple[2])

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
