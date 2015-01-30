#!/usr/bin/env python3




def test_classifier(test_set,classifier):
  correct_results = {'pos' : 0, 'neg': 0, 'neu': 0}
  incorrect_results = {'pos' : 0, 'neg': 0, 'neu': 0}

  n = [0,0,0]
  for item in test_set:
    classification = classifier.classify(item[0])
    #print (str(item)+','+classification)
    if classification == item[1]:
      correct_results[item[1]] += 1
    else:
      incorrect_results[item[1]] += 1

  return (correct_results,incorrect_results)

def classifier(input):
  sentiment = {}
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

  for tuple in input:
    for pattern in patterns:
      years.add(tuple[0])
      try:
        results[pattern.pattern][tuple[0]] += len(pattern.findall(tuple[2]))
      except:
        results[pattern.pattern][tuple[0]] = len(pattern.findall(tuple[2]))

    # Sentiment analysis:
    blob = TextBlob(tuple[2],classifier=cl)
    polarity = 0.0
    for sentence in blob.sentences:
      polarity = 0
      sent = sentence.classify()
      print(sentence,end=',')
      print(sent)
      if sent == 'pos':
        polarity = 1
      elif sent == 'neg':
        polarity = -1
      if (tuple[1].startswith('Wollongong')):
        sentiment['Wollongong'] += polarity
        n['Wollongong'] += 1
      elif (tuple[1].startswith('Kiama')):
        sentiment['Kiama'] += polarity
        n['Kiama'] += 1
      else:
        sentiment['other'] += polarity
        n['other'] += 1


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
