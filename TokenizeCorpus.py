
from nltk.tokenize import sent_tokenize, word_tokenize
import sys, os


source = 'BuildCorpus'
dump = 'Tokens'



if not os.path.exists(dump):
    os.makedirs(dump)
    print('created folder to dump corpus:{}'.format(dump))


def generateTokens(txt, count):
    tokens = word_tokenize(txt)
    tokensList = ""

    for t in tokens:
        tokensList += t + "\n"
    try:
        with open("{}/{}.txt".format(dump, count), 'w') as dumpFile:
            dumpFile.write(tokensList)
        print('successfully Tokens Build : count = {}\r'.format(count), end = '')
            #print(tokens)
    except Exception as e:
        print()
        print(e)
    return None

for (dirpath, dirnames, filenames) in os.walk(source):
    for f in filenames:
        try:
            filename = "{}/{}".format(dirpath, f)
            with open(filename, 'r') as corpusFile:
                text = corpusFile.read()
                count = f.split('.')[0]
                generateTokens(text, count)
        except Exception as e:
            print(e)
            
            
            
            
