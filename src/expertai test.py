from expertai.nlapi.cloud.client import ExpertAiClient
import json
# import pkgutil
# package=expertai
# for importer, modname, ispkg in pkgutil.walk_packages(path=package.__path__,
#                                                       prefix=package.__name__+'.',
#                                                       onerror=lambda x: None):
#     print(modname)

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["EAI_USERNAME"] = os.getenv('EAI_NAME')
os.environ["EAI_PASSWORD"] = os.getenv('EAI_PASS')

LANGUAGE = 'en'
PLACEHOLDER_TEXT = 'Today is a good day. I love to go to mountain.'
PLACEHOLDER_TEXT2 = 'I hate life'

# EAI NL API
client = ExpertAiClient()

document = client.specific_resource_analysis(
    body={"document": {"text": PLACEHOLDER_TEXT2}},
    params={'language': LANGUAGE, 'resource': 'sentiment'})
print(document.sentiment.overall)