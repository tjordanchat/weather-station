import os
import math
import urllib2
from xml.dom import minidom
import time
import datetime
import codecs
import json
import subprocess
from pprint import pprint

with open('news.json') as f:
    news = json.load(f)

# Open SVG to process
output = codecs.open('news.svg', 'r', encoding='utf-8').read()

story = [0 for i in range(10)]
for j in range(10):
  story[j]=news["articles"][j]["title"] 

line=0
for s in range(10):
  if line > 14:
  	break
  length = len(story[s])-1
  it=int(length/20)+1
  for x in range(it):
    if x > 0:
      buf=" ... "
    else:
      buf=" * "
    l=int(x*20)
    if length-l < 20:
      h=length
    else:
      h=int((x+1)*20)
    output = output.replace('__NEWS_LINE_'+str(line)+'__',buf+story[s][l:h]) 
    line=line+1
    if line > 14:
    	break

codecs.open('news-processed.svg', 'w', encoding='utf-8').write(output)

f.close()
