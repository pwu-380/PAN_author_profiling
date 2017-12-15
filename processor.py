__author__ = 'Peter'

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

NO_URLS = False
NO_TAGS = False
NO_PUNCT = False
NO_NUM = False
NO_STOPWORDS = False
STEMMING = True

SOURCE_FILE = "data_clean/PAN2017_author_text.txt"
save_string = "data_postprocessed/PAN2017_author_text"

if NO_URLS:
    save_string += "_rmURL"
if NO_TAGS:
    save_string += "_rmTag"
if NO_PUNCT:
    save_string += "_rmPunc"
if NO_NUM:
    save_string += "_rmNo"
if NO_STOPWORDS:
    save_string += "_rmStop"
if STEMMING:
    save_string += "_stem"

save_string += ".txt"

f1 = open(SOURCE_FILE, 'r')
s1 = open(save_string, 'w')

def isURL(token):
    if 'http' in token:
        return True
    else:
        return False

def isTag(token):
    if '#' in token:
        return True
    elif '@' in token:
        return True
    else:
        return False

def isPunct(token):
    if re.search('\W',token) == None:
        return False
    else:
        return True

def isNum(token):
    try:
        float(s)
        return True
    except ValueError:
        return  False

def isStopword(token):
    if (token not in stopwords.words('english')):
        return False
    else:
        return True

stemmer = PorterStemmer()

for line in f1:
    new_token_list = []
    token_list = line.rstrip().split(" ")
    for token in token_list:
        rm = False
        if NO_URLS and isURL(token):
            rm = True
        elif NO_TAGS and isTag(token):
            rm = True
        elif NO_PUNCT and isPunct(token):
            rm = True
        elif NO_NUM and isNum(token):
            rm = True
        elif NO_STOPWORDS and isStopword(token):
            rm = True

        if not rm:
            if STEMMING:
                new_token_list.append(stemmer.stem(token))
            else:
                new_token_list.append(token)

    s1.write(" ".join(s.encode('ascii', 'ignore') for s in new_token_list) + '\n')

f1.close()
s1.close()