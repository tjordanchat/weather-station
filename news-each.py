import os
import math
import urllib2
from xml.dom import minidom
import time
import cgi
import datetime
import codecs
import json
import subprocess
import array
from pprint import pprint

with open('news.json') as f:
    news = json.load(f)
f.close()
  
num_items=len(news["articles"])
story=["" for i in range(num_items)]
out=["" for i in range(num_items)]
for j in range(num_items):
  out[j] = codecs.open('news-each.svg', 'r', encoding='utf-8').read()
  t=news["articles"][j]["description"] 
  if t == None:
    story[j]=(news["articles"][j]["title"]).replace('\\','')
  else:
    story[j]=(news["articles"][j]["description"]).replace('\\','')
  sl=int(len(story[j]))
  paragraph=""
  index=0
  max=24
  om=0
  pi=0
  for k in range(sl):
    if story[j][k] == ' ':
      if pi < max:
        mark=k+1
      else:
        if index == 0:
           st=story[j][om:mark]
           st=st.replace("\\","")
           st=st.replace("\"","'")
           s = cgi.escape(st)
           paragraph=paragraph+'<tspan font="Courier"  x="0" dy="1.2em" text-anchor="start">'+s+'</tspan>'
           index=1
        else:
           st=story[j][om:mark]
           st=st.replace("\\","")
           st=st.replace("\"","'")
           s = cgi.escape(st)
           paragraph=paragraph+'<tspan font="Courier" x="0" dy="1.2em" text-anchor="start">'+s+'</tspan>'
        om=mark
        pi=0
    pi=pi+1
  st=story[j][om:sl]
  st=st.replace("\\","")
  st=st.replace("\"","'")
  s = cgi.escape(st)
  paragraph=paragraph+'<tspan font="Courier" x="0" dy="1.2em" text-anchor="start">'+s+'</tspan>'
  out[j] = out[j].replace('__NEWS_TITLE__',paragraph)
  c=codecs.open('news/news-processed_'+str(j)+'.svg', 'w', encoding='utf-8').write(out[j])
  pi=0

