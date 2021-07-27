from bs4 import BeautifulSoup
import requests
import os, sys
import string


listOfUrls = [
           
           

           'https://www.gutenberg.org/files/203/203-h/203-h.htm',
           'https://www.gutenberg.org/files/863/863-h/863-h.htm',
           'https://www.gutenberg.org/files/25344/25344-h/25344-h.htm',
           'https://www.gutenberg.org/files/1727/1727-h/1727-h.htm',
           'https://www.gutenberg.org/files/23042/23042-h/23042-h.htm',
           'https://www.gutenberg.org/files/1998/1998-h/1998-h.htm',
           'https://www.gutenberg.org/files/829/829-h/829-h.htm',
           'https://www.gutenberg.org/files/2814/2814-h/2814-h.htm',
           'https://www.gutenberg.org/files/36/36-h/36-h.htm',
           'https://www.gutenberg.org/files/43453/43453-h/43453-h.htm',
           'https://www.gutenberg.org/files/766/766-h/766-h.htm',
           'https://www.gutenberg.org/ebooks/730',
           'https://www.gutenberg.org/files/28054/28054-h/28054-h.htm',
           
           

           

           'https://www.gutenberg.org/files/2413/2413-h/2413-h.htm',
           'https://www.gutenberg.org/files/40074/40074-h/40074-h.htm',
           'https://www.gutenberg.org/files/2638/2638-h/2638-h.htm',
           'https://www.gutenberg.org/files/146/146-h/146-h.htm',
           'https://www.gutenberg.org/files/8799/8799-h/8799-h.htm',
           'https://www.gutenberg.org/files/141/141-h/141-h.htm',
           'https://www.gutenberg.org/files/10676/10676-h/10676-h.htm',
           'https://www.gutenberg.org/files/16643/16643-h/16643-h.htm',
           'https://www.gutenberg.org/files/1023/1023-h/1023-h.htm',
           'https://www.gutenberg.org/files/7142/7142-h/7142-h.htm',
           'https://www.gutenberg.org/files/24518/24518-h/24518-h.htm',
           'https://www.gutenberg.org/files/22120/22120-h/22120-h.htm',
           'https://www.gutenberg.org/files/1946/1946-h/1946-h.htm',
           'https://www.gutenberg.org/files/2000/2000-h/2000-h.htm',
           'https://www.gutenberg.org/files/7178/7178-h/7178-h.htm',
           'https://www.gutenberg.org/files/10800/10800-h/10800-h.htm',
           'https://www.gutenberg.org/files/4280/4280-h/4280-h.htm',
           

           'https://www.gutenberg.org/files/82/82-h/82-h.htm',
           'https://www.gutenberg.org/files/45376/45376-h/45376-h.htm',
           'https://www.gutenberg.org/files/2707/2707-h/2707-h.htm',
           'https://www.gutenberg.org/files/49513/49513-h/49513-h.htm',
           'https://www.gutenberg.org/files/57764/57764-h/57764-h.htm',
           'https://www.gutenberg.org/files/8117/8117-h/8117-h.htm',
           'https://www.gutenberg.org/files/15474/15474-h/15474-h.htm',
           'https://www.gutenberg.org/files/16966/16966-h/16966-h.htm',
           'https://www.gutenberg.org/files/55201/55201-h/55201-h.htm',
           'https://www.gutenberg.org/files/155/155-h/155-h.htm',
           'https://www.gutenberg.org/files/228/228-h/228-h.htm',
           'https://www.gutenberg.org/files/968/968-h/968-h.htm',
           'https://www.gutenberg.org/files/3177/3177-h/3177-h.htm',
           'https://www.gutenberg.org/files/155/155-h/155-h.htm',
           'https://www.gutenberg.org/files/228/228-h/228-h.htm',
           'https://www.gutenberg.org/files/968/968-h/968-h.htm',



]

#wikipedia Url
_wikiurl = "https://en.wikipedia.org/wiki/Special:Random"


# Corpus size initialize to Zero
totalCorpusSize = 0
count= 0

dumpPath = 'BuildCorpus'


def cleanPunct(txt):
    no_punct = [words for words in text if words not in string.punctuation]
    words_wo_punct = ''.join(no_punct)
    return words_wo_punct

if not os.path.exists(dumpPath):
    os.makedirs(dumpPath)
    print('created folder to dump corpus:{}'.format(dumpPath))
    

print("Start Building corpus.....")
for wikiurl in listOfUrls:
    try:
        res = requests.get(wikiurl)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')

        text = ""

        for data in soup.find_all("p"):
            #text += data.get_text().encode('utf-8')
            text += data.get_text()
        _text = cleanPunct(text)

    except Exception as e:
        print(e)
    finally:
        # current corpus
        #title = soup.title.string.encode('utf-8').lstrip().rstrip()
        size = len(_text.split())

        with open("{}/{}.txt".format(dumpPath, count), 'w') as file1:
            file1.write(_text)
        count+= 1

        # total corpus size 
        totalCorpusSize += size

        print("Corpus Count={}, Corpus size = {}".format(count, size))

# print the total size of Corpus
print("Total size of the corpus = {}".format(totalCorpusSize))

