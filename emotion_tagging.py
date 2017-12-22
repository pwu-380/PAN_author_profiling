import pandas as pd

#This uses Niko Colneric's pretrained emotion predictor models: https://github.com/nikicc/twitter-emotion-recognition
from emotion_predictor import EmotionPredictor


TWEET_FILE = 'PAN2017_author_text_tagger_input.txt'

f1 = open(TWEET_FILE, 'r')

model = EmotionPredictor(classification='ekman', setting='mc', use_unison_model=True)
linen = -1
batch = []

for line in f1:
    linen += 1
    if linen == 0:
        print line
    elif linen == 101:
        predictions = model.predict_classes(batch)
        print (predictions.to_csv(columns=['Emotion'], index=False))
        print line
        batch = []
        linen = 0
    else:
        batch.append(line)

predictions = model.predict_classes(batch)
print (predictions.to_csv(columns=['Emotion'], index=False))

f1.close()