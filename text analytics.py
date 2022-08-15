# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 20:28:03 2022

@author: Bharath kuamr reddy
"""

#### news text sentiment analysis
pip install newsapi
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='c0004afc5d1a411ead0ef211fa0205d4')
th = newsapi.get_top_headlines(q='cricket',language="en",page_size=20)
th
type(th)
th.keys()
th.values()
type(th['articles'])
th['articles']
txt = th['articles'][0]['description']
txt
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
sid.polarity_scores(txt)
lis = th['articles']
lis
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
for i in lis:
    txt = i['title']
    res = sid.polarity_scores(txt)
    print(res)
    


from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
txt = "There's so much to love about Matt Reeves' The Batman: the characters, the cinematography, the stellar soundscape, the incredible world-building. The screenplay could have been a little tighter, though."
res = sid.polarity_scores(txt)
type(res)
print(res)











