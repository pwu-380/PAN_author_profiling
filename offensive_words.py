#This script tallies the proportion of offensive words in each "document"
#Corpus from CMU blog

#Profanity corpus
PROFANE_FILE = 'data_raw/bad-words.txt'
#Using a processed text file with punctuation stripped
TEXT_FILE = 'data_postprocessed/PAN2017_author_text_rmPunc.txt'
SAVE_FILE = 'data_clean/PAN2017_author_offensive.txt'

profanities = []

f1 = open(PROFANE_FILE, 'r')
f2 = open(TEXT_FILE, 'r')
s1 = open(SAVE_FILE, 'w')

#Create list of profanities
for line in f1:
    profanities.append(line.rstrip())

f1.close()

#Calculates proportion of profanities in each line
for line in f2:
    count = 0.0
    words = line.split(' ')
    nwords = len(words)

    for word in words:
        if word in profanities:
            count += 1

    s1.write(str(count/nwords) + '\n')

f1.close()
s1.close()