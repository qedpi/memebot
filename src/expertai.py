#may need to set env vars
#import os
#os.environ["EAI_USERNAME"] = 'comacwilliam@crimson.ua.edu'
#os.environ["EAI_PASSWORD"] = ''

from expertai import *
from expertai.nlapi.cloud.client import ExpertAiClient
myClient = ExpertAiClient()

text = 'Facebook is looking at buying an American startup for $6 million based in Springfield, IL .'
lang= 'en'

#document = myClient.specific_resource_analysis(
#    body={"document": {"text": text}},
#    params={'language': lang, 'resource': 'disambiguation'}
#  )

print("A")
