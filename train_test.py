#!/usr/bin/env python3

import input

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier



def test_classifier(test_set,classifier):
  correct_results = {'pos' : 0, 'neg': 0, 'neu': 0}
  incorrect_results = {'pos' : 0, 'neg': 0, 'neu': 0}

  n = [0,0,0]
  for item in test_set:
    classification = classifier.classify(item[0])
    print(item)
    #print (str(item)+','+classification)
    if classification == item[1]:
      correct_results[item[1]] += 1
    else:
      incorrect_results[item[1]] += 1

  return (correct_results,incorrect_results)

# now build a custom classifier

if __name__ == '__main__':
  train = input.load_set(['training_2_cleaned_analysed.txt'])
  test = input.load_set(['test_cleaned_analysed.txt'])

  cl = NaiveBayesClassifier(train)

  (correct_results, incorrect_results) = test_classifier(test,cl)

  print('category,number correct,number incorrect,total number')
  for category in correct_results:
    print(category+','+str(correct_results[category])+','+str(incorrect_results[category])+','+str(correct_results[category] + incorrect_results[category]))
