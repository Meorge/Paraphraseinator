from ppi import Paraphraseinator
import json
import random

import os
from dotenv import load_dotenv


load_dotenv()
KEY = os.getenv('THES_KEY')

# quotes.json is from https://github.com/JamesFT/Database-Quotes-JSON
f = open("quotes.json", "r")
quotes = json.load(f)
f.close()


subset_quotes = random.sample(quotes, 5)

p = Paraphraseinator(KEY)

for i in subset_quotes:
    print(f"\"{p.paraphraseinate(i['quoteText'])}\"\n\t-- {i['quoteAuthor']}\n")
