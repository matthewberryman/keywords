#!/usr/local/bin/python3

import input, re, random

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

years = set()

random.seed()

keywords = []; patterns = []; results = {}; sentiment = {}
positive_words = set(); negative_words = set(); negation_words = set()




# now build a custom classifier

train = input.load_set(['training_2_cleaned_analysed.txt'])

cl = NaiveBayesClassifier(train)

import train_test

(correct_results, incorrect_results) = train_test.test_classifier('test_cleaned_analysed.txt',cl)

print('category,number correct,number incorrect,total number')
for category in correct_results:
  print(category+','+str(correct_results[category])+','+str(incorrect_results[category])+','+str(correct_results[category] + incorrect_results[category]))

l = input.anzns('anzns.txt')

#l += input.factiva('factiva.txt')]




#print('Len')
#print(len(wollongong_articles))
#print(len(kiama_articles))
#print(len(other_articles))

#print(wollongong_articles)

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

for key in sentiment.keys():
  sentiment[key] = sentiment[key]/n[key]

print(n)
print(sentiment)

print('',end=',')

years = list(years)
years.sort()

#for year in years:
#    print(year,end=',')

#print()

#for pattern in patterns:
#    print(pattern.pattern,end=',')
#    for year in years:
#      print(results[pattern.pattern][year],end=',')
#    print()

#print()

#print()
