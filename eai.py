#set env vars
import os
os.environ["EAI_USERNAME"] = 'comacwilliam@crimson.ua.edu'
os.environ["EAI_PASSWORD"] = 'Soccer05!'

from textblob import TextBlob
import expertai
from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()


# Output range = [-100,100]. 100 = very positive. -100 = very negative.
def analyzeSent(text):
  text = str(text)
  if len(text) < 4:
    return(0.0)
  
  b = TextBlob(text)
  language = b.detect_language()

  badList = ['ru', 'uk', 'su', 'sr', 'tl', 'pt', 'fi']
  if language in badList:
    return(0.0)

  try:
    output = client.specific_resource_analysis(
      body={"document": {"text": text}}, 
      params={'language': language, 'resource': 'sentiment'
  })
  except:
    output = client.specific_resource_analysis(
      body={"document": {"text": text}}, 
      params={'language': 'en', 'resource': 'sentiment'
  })
  return(output.sentiment.overall)


#grab dataset
import pandas as pd
dataset = 'memegenerator.csv'
df = pd.read_csv(dataset)
saved_column = df.AlternateText
textList = list(saved_column)

sentList = []
retDF = pd.DataFrame(columns=['Text', 'Sentiment'])

for i in range(57651, len(textList)):
  try:
    score = analyzeSent(textList[i])
  except:
    score = 0.0
  print(i, textList[i], score)
  new_row = {'Text': textList[i], 'Sentiment': score}
  retDF = retDF.append(new_row, ignore_index=True)
  retDF.to_csv('memegen11.csv')




#print(sentList, len(sentList), len(textList))
#df['SentimentAnalysis'] = sentList
#df.to_csv('memegenerator1.csv')

