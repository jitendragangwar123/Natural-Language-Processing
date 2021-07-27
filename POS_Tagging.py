import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
_stopwords = set(stopwords.words('english'))
import json
import os
import string

corpusSource = 'BuildCorpus'
posDump = 'POSTagging'

def POStagging(txt):
    tokenized = sent_tokenize(txt)

    for i in tokenized:	
        # Word tokenizers is used to find the words
        # and punctuation in a string
        wordsList = nltk.word_tokenize(i)

        # removing stop words from wordList
        wordsList = [w for w in wordsList if not w in _stopwords]

        # Using a Tagger. Which is part-of-speech
        # tagger or POS-tagger.
        tagged = nltk.pos_tag(wordsList)
        taggedString = json.dumps(tagged)
        return taggedString

if __name__ == "__main__":
    for (dirpath, dirnames, filenames) in os.walk(corpusSource):
        for f in filenames:
            filename = "{}/{}".format(corpusSource, f)
            ID = f.split('.')[0]

            with open( filename, 'r' ) as F:
                txt = F.read()
                tag = POStagging(txt)
                dumpFile = "{}/{}.txt".format(posDump, ID)
                with open(dumpFile, 'w') as _F:
                    _F.write(tag)
            print('POS tagging Successfully Build = {}'.format(f))
