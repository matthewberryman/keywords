#!/usr/bin/env python3

import re

training_set = set()

test_set = set()

for line in open('training_2.txt','r'):
    line = line.rstrip()
    training_set.add(line)

for line in open('test.txt','r'):
    if (line.rstrip() not in training_set) and (line.rstrip().endswith(',')):
        test_set.add(line.rstrip())

training = open('training_2_cleaned.txt','w')
test = open('test_cleaned.txt','w')

for line in training_set:
    print(line,file=training)

for line in test_set:
    if (not re.search('Credit:',line)) and (not re.search('Title:',line)):
        print(line,file=test)
