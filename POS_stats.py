#This is taking the PAN 2017 dataset, tokenizing the files and combining the result in one line terminated file with the
#text samples and one line terminated file with the gender labels

import re                                           #The XML is pretty simple so just parsing with regex
from collections import namedtuple

#These are the location of the PAN files
POS_FILE = 'data_clean/PAN2017_author_text_tagger_output.txt'

#Save directory
SAVE_DIR = 'data_clean'
#Filename for the processed text
SAVE_TEXT = 'PAN2017_author_POS_stats.txt'

f1 = open(POS_FILE, 'r')
wtext = open(SAVE_DIR + '/' + SAVE_TEXT, 'w')

#Interested in coordinating conjunctions, determiners, prepositions, adjectives, nouns, pronouns,
#adverbs, interjections and verbs
#i.e. _CC, _DT, _IN, _JJ, _NN, _PRP, _RB, _UH _VB

pos_counts = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]    #In above order

#Takes the annotations file, looks up the user key and opens that user's tweet corpus
linen = 100

for line in f1:
    linen += 1
    if linen == 101:
        linen = 0
        total = sum(pos_counts)
        for i in range(len(pos_counts)):
            wtext.write(str(pos_counts[i]/total) + " ")
            pos_counts[i] = 0.0
        wtext.write('\n')
    else:
        count = len(re.findall(ur'_CC', line))
        pos_counts[0] += count
        count = len(re.findall(ur'_DT', line))
        pos_counts[1] += count
        count = len(re.findall(ur'_IN', line))
        pos_counts[2] += count
        count = len(re.findall(ur'_JJ', line))
        pos_counts[3] += count
        count = len(re.findall(ur'_NN', line))
        pos_counts[4] += count
        count = len(re.findall(ur'_PRP', line))
        pos_counts[5] += count
        count = len(re.findall(ur'_RB', line))
        pos_counts[6] += count
        count = len(re.findall(ur'_UH', line))
        pos_counts[7] += count
        count = len(re.findall(ur'_VB', line))
        pos_counts[8] += count

total = sum(pos_counts)
for i in range(len(pos_counts)):
    wtext.write(str(pos_counts[i]/total) + " ")

f1.close()
wtext.close()