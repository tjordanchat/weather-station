import os
import math
import urllib2
from xml.dom import minidom
import time
import datetime
import codecs
import json
import subprocess
import array
from pprint import pprint

with open('news.json') as f:
    news = json.load(f)
  
num_items=len(news["articles"])
story=["" for i in range(num_items)]
out=["" for i in range(num_items)]
for j in range(num_items):
  out[j] = codecs.open('news-each.svg', 'r', encoding='utf-8').read()
  story[j]=news["articles"][j]["description"] 
  sl=len(story[j])
  paragraph=""
  index=0
  max=18
  om=0
  for k in range(sl):
    if story[j][k] == ' ':
      if index < max:
        mark=k
      else:
        if index == 0:
           paragraph=paragraph+'<tspan x="0" dy="1.2em" text-anchor="start"> * '+story[j][om:mark]+'</tspan>'
        else:
           paragraph=paragraph+'<tspan x="0" dy="1.2em" text-anchor="start">'+story[j][om:mark]+'</tspan>'
        om=mark
        index=0
    index=index+1
  out[j] = out[j].replace('__NEWS_TITLE__',paragraph)
  codecs.open('news/news-processed_'+str(j)+'.svg', 'w', encoding='utf-8').write(out[j])

f.close()
