#set env vars
import os
os.environ["EAI_USERNAME"] = 'comacwilliam@crimson.ua.edu'
os.environ["EAI_PASSWORD"] = ''

import expertai
from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()
language= 'en'

# Output range = [-100,100]. 100 = very positive. -100 = very negative.
def analyzeSent(text):
  output = client.specific_resource_analysis(
    body={"document": {"text": text}}, 
    params={'language': language, 'resource': 'sentiment'
})
  return(output.sentiment.overall)

text = 'I am very happy!!'
analyzeSent(text)

#grab dataset
import pandas as pd
dataset = 'memegenerator.csv'
df = pd.read_csv(dataset)
saved_column = df.AlternateText
textList = list(saved_column)

sentList = []
for i in range(0, len(textList):
  score = analyzeSent(textList[i])
  sentList.append(score)

print(sentList, len(sentList))
df['SentimentAnalysis'] = sentList
df.to_csv('memegenerator1.csv')

