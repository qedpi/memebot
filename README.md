# memebot
bot that composes original memes based on sentiment and semantics of conversation!

# dev instructions
(from https://stackoverflow.com/questions/19135867/what-is-pips-equivalent-of-npm-install-package-save-dev)
- pip install -r requirements.txt
- pip freeze > requirements.txt

## [pipreqs](https://github.com/bndr/pipreqs)
- pip install pipreqs
- pipreqs <path of requirements.txt>
 - pipreqs --force . (create reqs in curdur, overwrite if necessary)

# expert.ai integration
- pip install -U expertai-nlapi
- set uname & pass in os.env
- init client