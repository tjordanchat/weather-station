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
print(num_items)
story=["" for i in range(num_items)]
out=["" for i in range(num_items)]
for j in range(num_items):
  print(j)
  story[j]=news["articles"][j]["title"] 
  out[j] = codecs.open('news-each.svg', 'r', encoding='utf-8').read()
  out[j] = out[j].replace('__NEWS_TITLE__',story[j])
  codecs.open('news/news-processed_'+str(j)+'.svg', 'w', encoding='utf-8').write(out[j])

f.close()
