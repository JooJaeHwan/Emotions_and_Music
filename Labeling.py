import pandas as pd
from konlpy.tag import Mecab, Kkma, Okt
K_tagger = Kkma()
label = []

df = pd.read_csv("./Data.csv", index_col=0)
emotion_df = pd.read_csv('./emotion.csv', index_col=0)


for i in range(len(df)):
    sad_score = 0
    pleasure_score = 0
    flutter_score = 0
    joy_score = 0
    angry_score = 0
    love_score = 0
    resentment_score = 0
    longing_score = 0
    disappointment_score = 0
    hope_score = 0
    worry_score = 0
    K_token = K_tagger.morphs(df.iloc[i,0]) 
    for k in K_token:
        if len(emotion_df.loc[emotion_df["word"] == k]) == 0:
            continue
        sad_score += float(emotion_df.loc[emotion_df["word"] == k]["sad"].iloc[0])
        pleasure_score += float(emotion_df.loc[emotion_df["word"] == k]["pleasure"].iloc[0])
        flutter_score += float(emotion_df.loc[emotion_df["word"] == k]["flutter"].iloc[0])
        joy_score += float(emotion_df.loc[emotion_df["word"] == k]["joy"].iloc[0])
        angry_score += float(emotion_df.loc[emotion_df["word"] == k]["angry"].iloc[0])
        love_score += float(emotion_df.loc[emotion_df["word"] == k]["love"].iloc[0])
        resentment_score += float(emotion_df.loc[emotion_df["word"] == k]["resentment"].iloc[0])
        longing_score += float(emotion_df.loc[emotion_df["word"] == k]["longing"].iloc[0])
        disappointment_score += float(emotion_df.loc[emotion_df["word"] == k]["disappointment"].iloc[0])
        hope_score += float(emotion_df.loc[emotion_df["word"] == k]["hope"].iloc[0])
        worry_score += float(emotion_df.loc[emotion_df["word"] == k]["worry"].iloc[0])
    if max(sad_score, pleasure_score, flutter_score, joy_score, angry_score, love_score, resentment_score, longing_score, disappointment_score, hope_score, worry_score) == sad_score:
        label.append(0)
    elif max(sad_score, pleasure_score, flutter_score, joy_score, angry_score, love_score, resentment_score, longing_score, disappointment_score, hope_score, worry_score) == pleasure_score:
        label.append(1)
    elif max(sad_score, pleasure_score, flutter_score, joy_score, angry_score, love_score, resentment_score, longing_score, disappointment_score, hope_score, worry_score) == flutter_score:
        label.append(2)
    elif max(sad_score, pleasure_score, flutter_score, joy_score, angry_score, love_score, resentment_score, longing_score, disappointment_score, hope_score, worry_score) == joy_score:
        label.append(3)
    elif max(sad_score, pleasure_score, flutter_score, joy_score, angry_score, love_score, resentment_score, longing_score, disappointment_score, hope_score, worry_score) == angry_score:
        label.append(4)
    elif max(sad_score, pleasure_score, flutter_score, joy_score, angry_score, love_score, resentment_score, longing_score, disappointment_score, hope_score, worry_score) == love_score:
        label.append(5)
    elif max(sad_score, pleasure_score, flutter_score, joy_score, angry_score, love_score, resentment_score, longing_score, disappointment_score, hope_score, worry_score) == resentment_score:
        label.append(6)
    elif max(sad_score, pleasure_score, flutter_score, joy_score, angry_score, love_score, resentment_score, longing_score, disappointment_score, hope_score, worry_score) == longing_score:
        label.append(7)
    elif max(sad_score, pleasure_score, flutter_score, joy_score, angry_score, love_score, resentment_score, longing_score, disappointment_score, hope_score, worry_score) == disappointment_score:
        label.append(8)
    elif max(sad_score, pleasure_score, flutter_score, joy_score, angry_score, love_score, resentment_score, longing_score, disappointment_score, hope_score, worry_score) == hope_score:
        label.append(9)
    elif max(sad_score, pleasure_score, flutter_score, joy_score, angry_score, love_score, resentment_score, longing_score, disappointment_score, hope_score, worry_score) == worry_score:
        label.append(10)
    print(f'{i+1}/{len(df)}')

df = pd.concat([df, pd.Series(label)], axis=1)
df.rename(columns={0:'label'})
df.to_csv('./Kkma.csv')
