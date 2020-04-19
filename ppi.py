from thesaurus import Thesaurus
import random
import mcw
import string


punctuation = ['.', ',', '!', '?', ')', '(', ')', ':', ';']

class Paraphraseinator(object):
    def __init__(self, key):
        self.key = key
        self.extras = False
        self.thes = Thesaurus(self.key, self.extras)

    def paraphraseinate(self, text, originality=0.5):
        list_of_words = text.split()
        new_list_of_words = []

        for w in list_of_words:
            word_without_punct = w.translate(str.maketrans('', '', string.punctuation))
            if word_without_punct.lower() in mcw.most_common_words or random.random() > originality:
                new_list_of_words.append(w)
                continue

            word_info = self.thes.get_info(word_without_punct)
            if word_info is None:
                new_list_of_words.append(w)
                continue


            word_syns = word_info[0].synonyms
            
            
            syn_index = random.randint(0, len(word_syns) - 1)
            syn = word_syns[syn_index]

            # print(f"Choosing {syn} as synonym for {word_without_punct}")

            if w[-1] in punctuation:
                syn += w[-1]

            if w[0].isupper():
                syn = syn.capitalize()

            new_list_of_words.append(syn)

        return ' '.join(new_list_of_words)
