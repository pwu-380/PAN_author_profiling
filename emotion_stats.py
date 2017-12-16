#These are the location of the EMO files
EMO_FILE = 'data_raw/tweet_emotions.txt'

#Save directory
SAVE_DIR = 'data_clean'
#Filename for the processed text
SAVE_TEXT = 'e-m-o-t-i-o-n.txt'

f1 = open(EMO_FILE, 'r')
wtext = open(SAVE_DIR + '/' + SAVE_TEXT, 'w')

#Each tweet was classified as predominantly Anger, Disgust, Fear, Joy, Sadness, Surprise
#In above order:

emo_counts = [0, 0, 0, 0, 0, 0]    #In above order

#Takes the annotations file, looks up the user key and opens that user's tweet corpus

for line in f1:
    if line.rstrip() == "Emotion":
        for n in emo_counts:
            wtext.write(str(n) + " ")
        emo_counts = [0, 0, 0, 0, 0, 0]
        wtext.write('\n')
    elif line.rstrip() == "Anger":
        emo_counts[0] += 1
    elif line.rstrip() == "Disgust":
        emo_counts[1] += 1
    elif line.rstrip() == "Fear":
        emo_counts[2] += 1
    elif line.rstrip() == "Joy":
        emo_counts[3] += 1
    elif line.rstrip() == "Sadness":
        emo_counts[4] += 1
    elif line.rstrip() == "Surprise":
        emo_counts[5] += 1

for n in emo_counts:
    wtext.write(str(n) + " ")

f1.close()
wtext.close()