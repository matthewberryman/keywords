#!/usr/local/bin/python3

import input, re, random

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

years = set()

random.seed()

keywords = []; patterns = []; results = {}; sentiment = {}
positive_words = set(); negative_words = set(); negation_words = set()

# input keywords
for keyword in open('keywords.txt','r'):
  patterns.append(re.compile(keyword.rstrip(),re.IGNORECASE))
  results[patterns[-1].pattern] = {}

# input positive, negative, and negation words for sentiment analysis
for positive_word in open('positive_words.txt','r'):
  positive_words.add(positive_word.rstrip())
for negative_word in open('negative_words.txt','r'):
  negative_words.add(negative_word.rstrip())
for negation_word in open('negation_words.txt','r'):
  negation_words.add(negation_word.rstrip())

# now build a custom classifier

train = []

for positive_word in positive_words:
  train.append((positive_word,'pos'))
  for negation_word in negation_words:
    train.append((negation_word + ' ' + positive_word,'neg'))
for negative_word in negative_words:
  train.append((negative_word,'neg'))
  for negation_word in negation_words:
    train.append((negation_word + ' ' + negative_word,'pos'))

cl = NaiveBayesClassifier(train)



l = input.anzns('anzns.txt')

#l += input.factiva('factiva.txt')]

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
  for pattern in patterns:
    years.add(tuple[0])
    try:
      results[pattern.pattern][tuple[0]] += len(pattern.findall(tuple[2]))
    except:
      results[pattern.pattern][tuple[0]] = len(pattern.findall(tuple[2]))

  # Sentiment analysis:
  blob = TextBlob(tuple[2])
  polarity = 0.0
  for sentence in blob.sentences:
    polarity += sentence.sentiment.polarity
    if sentence.sentiment.polarity >= 0.0:
      positive_phrases.write(tuple[2])
    else:
      negative_phrases.write(tuple[2])

#  sent = cl.classify(tuple[2])
#  polarity = 0
#  if sent == 'pos':
#    positive_phrases.write(tuple[2])
#    polarity = 1
#  else:
#    negative_phrases.write(tuple[2])
#    polarity = -1
  if (tuple[1].startswith('Wollongong')):
    wollongong_articles.append(tuple[2])
    sentiment['Wollongong'] += polarity
    n['Wollongong'] += 1
  elif (tuple[1].startswith('Kiama')):
    kiama_articles.append(tuple[2])
    sentiment['Kiama'] += polarity
    n['Kiama'] += 1
  else:
    other_articles.append(tuple[2])
    sentiment['other'] += polarity
    n['other'] += 1

print('Len')
print(len(wollongong_articles))
print(len(kiama_articles))
print(len(other_articles))

print(wollongong_articles)

for i in range(6):
  wollongong_article = TextBlob(random.choice(wollongong_articles))
  kiama_article = TextBlob(kiama_articles[i])
  other_article = TextBlob(random.choice(other_articles))
  wollongong_text.write('Article ' + str(i) + ':\n')
  for sentence in wollongong_article.sentences:
    wollongong_text.write(sentence + ',\n')
  wollongong_text.write('\n')

  kiama_text.write('Article ' + str(i) + ':\n')
  for sentence in kiama_article.sentences:
    kiama_text.write(sentence + ',\n')
  kiama_text.write('\n')

  other_text.write('Article ' + str(i) + ':\n')
  for sentence in other_article.sentences:
    other_text.write(sentence + ',\n')
  other_text.write('\n')

for key in sentiment.keys():
  sentiment[key] = sentiment[key]/n[key]

print(n)
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
