import pandas as pd
from expertai.nlapi.cloud.client import ExpertAiClient
import os 
import pickle
from collections import defaultdict

df = pd.read_csv("data/memes_w_language.csv")
df = df[df['language'] == 'en'].reset_index()
print(df.shape)

os.environ["EAI_USERNAME"] = 'ilanazmmrmn7@gmail.com'
os.environ["EAI_PASSWORD"] = 'Madeleine&7'

client = ExpertAiClient()
language= 'en'
api_results = defaultdict(dict)
for i, row in df.iterrows():
    if i%100 == 0:
        print(i)
    text1 = row['Alternate Text']
    text2 = row['Base Meme Name']
    try:
        output1 = client.full_analysis(
            body={"document": {"text": text1}}, 
            params={'language': language})
    except:
        print(f'fail to analyze {text1}')
        output1 = 'API FAIL'
    try:
        output2 = client.full_analysis(
            body={"document": {"text": text2}}, 
            params={'language': language})
    except:
        print(f'fail to analyze {text2}')
        output2 = 'API FAIL'
    api_results[i]['Alternate Text'] = output1
    api_results[i]['Base Meme Name'] = output2
pickle.dump(api_results, open('api_results_dict.pkl', 'wb'))




