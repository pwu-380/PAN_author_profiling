#This is taking the PAN 2017 dataset, tokenizing the files and combining the result in one line terminated file with the
#text samples and one line terminated file with the gender labels

import re                                           #The XML is pretty simple so just parsing with regex
from nltk.tokenize.casual import TweetTokenizer     #Tokenizer

#These are the location of the PAN files
ANNOTATIONS_FILE = 'data_raw/truth.txt'
CORPUS = 'data_raw/Dataset'

#Save directory
SAVE_DIR = 'data_clean'
#Filename for the processed text
SAVE_TEXT = 'PAN2017_author_text.txt'
#Filename for the labels
SAVE_LABELS = 'PAN2017_author_genders.txt'

f1 = open(ANNOTATIONS_FILE, 'r')
wtext = open(SAVE_DIR + '/' + SAVE_TEXT, 'w')
wlabel = open(SAVE_DIR + '/' + SAVE_LABELS, 'w')


#Extracts all the tweets from an XML file
def parse_XML (file):
    text = ''
    for line in file:
        #Searches if it's a line with a tweet
        groups = re.search('\[CDATA\[(.*)\]\]', line)

        if groups is not None:
            #Extracts the tweet and lowercases it
            tweet = groups.group(1)
            tweet = tweet.lower()

            #Tokenizes the tweet
            tokens = TweetTokenizer().tokenize(tweet)
            tokenized = ' '.join(s.encode('ascii', 'ignore') for s in tokens)
            text = text + ' ' + tokenized

    return text[1:]

#Takes the annotations file, looks up the user key and opens that user's tweet corpus
for line in f1:
    annotations = line.split(':::')
    f2 = open(CORPUS + '/' + annotations[0] + '.xml', 'r')
    text = parse_XML(f2)                        #Gets all the user's tweets in a single line

    wtext.write(text + '\n')                    #Writes the tweets in one file and the matching gender in another
    wlabel.write(annotations[1] + '\n')

    f2.close()

f1.close()
wtext.close()
wlabel.close()