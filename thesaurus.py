import requests
import json, os

class Thesaurus(object):
    def __init__(self, api_key, extras):
        self.api_key = api_key
        self.extras = extras
        if self.extras: print(f"Create thesaurus with {api_key}")

    def get_info(self, word):
        cache = open("cache.json", "r+")
        raw_data = cache.read()

        data = {}

        cache.seek(0)
        if raw_data == "":
            if self.extras: print("Writing empty brackets")
            cache.write("{}")
            cache.seek(0)

        else:
            data = json.load(cache)
            cache.seek(0)

        if word in data:
            _json = data[word]

        else:
            req = requests.get(f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={self.api_key}")
            
            if req.status_code != 200:
                raise Exception(f"Status code {req.status_code}")

            _json = req.json()

            if len(_json) <= 0:
                return None

            if isinstance(_json[0], str):
                if self.extras: print(f"Didn't recognize {word} so here are suggestions - {_json}")
                return None

            
            
            data[word] = _json
            json.dump(data, cache)

        cache.close()

        return self._returnWordList(_json)




    def _returnWordList(self, _json):
        wordList = []
        for w in _json:
            newWord = Word(w)
            wordList.append(newWord)

        return wordList

class Word(object):
    def __init__(self, data):
        meta = data["meta"]
        self.word = meta["id"]
        self.uuid = meta["uuid"]
        self.stems = meta["stems"]

        # https://thispointer.com/python-convert-list-of-lists-or-nested-list-to-flat-list/
        self.synonyms = [ item for elem in meta["syns"] for item in elem]
        self.antonyms = [ item for elem in meta["ants"] for item in elem]

        self.offensive = meta["offensive"]

        self.functional_label = data["fl"]
        self.short_definitions = data["shortdef"]

