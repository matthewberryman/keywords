#!/usr/bin/env python3

import re

# Function for ensuring the tr

def cleanup_input_data(training_filename, test_filename):
  training_set = set()
  test_set = set()
  for line in open(training_filename,'r'):
    line = line.rstrip()
    training_set.add(line)

  for line in open(test_filename,'r'):
    if (line.rstrip() not in training_set) and (line.rstrip().endswith(',')):
      test_set.add(line.rstrip())

  training = open(training_filename[0:-4]+'_cleaned.txt','w')
  test = open(test_filename[0:-4]+'_cleaned.txt','w')

  for line in training_set:
    if (not re.search('Credit:',line)) and (not re.search('Title:',line)):
      print(line,file=training)

  for line in test_set:
    if (not re.search('Credit:',line)) and (not re.search('Title:',line)):
      print(line,file=test)

if __name__ == '__main__':
  cleanup_input_data('kiama_training.txt', 'kiama_test.txt')
  cleanup_input_data('wollongong_training.txt', 'wollongong_test.txt')
  cleanup_input_data('other_training.txt', 'other_test.txt')
