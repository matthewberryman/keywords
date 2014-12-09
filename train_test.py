#!/usr/bin/env python3


def test_classifier(filename, classifier):
  test_set = []
  correct_results = {'pos' : 0, 'neg': 0, 'neu': 0}
  incorrect_results = {'pos' : 0, 'neg': 0, 'neu': 0}

  n = [0,0,0]
  for line in open(filename,'r'):
    line = line.rstrip()
    if line.endswith(',-1'):
      test_set.append((line[0:-3],'neg'))
    elif line.endswith(',1'):
      test_set.append((line[0:-2],'pos'))
    elif line.endswith(',0'):
      test_set.append((line[0:-2],'neu'))

  for item in test_set:
    classification = classifier.classify(item[0])
    #print (str(item)+','+classification)
    if classification == item[1]:
      correct_results[item[1]] += 1
    else:
      incorrect_results[item[1]] += 1

  print('category,number correct,number incorrect,total number')
  for category in correct_results:
    print(category+','+str(correct_results[category])+','+str(incorrect_results[category])+','+str(correct_results[category] + incorrect_results[category]))
