import math
import urllib2
from xml.dom import minidom
import time
import datetime
import codecs
import json
from pprint import pprint

with open('DS.json') as f:
    data = json.load(f)

# Open SVG to process
output = codecs.open('svg_sun_up.svg', 'r', encoding='utf-8').read()

# ALL WORK DONE BELOW -->

offset=10
width=12
height=15

output = output.replace('WIDTH', str(width))
output = output.replace('HEIGHT', str(height))

sunriseTime=data["daily"]["data"][0]["sunriseTime"]
sunsetTime=data["daily"]["data"][0]["sunsetTime"]

sunrise_epoc = datetime.datetime.fromtimestamp(sunriseTime)
sunset_epoc = datetime.datetime.fromtimestamp(sunsetTime)

sunrise_sec=int(sunrise_epoc.strftime('%H'))*60*60+ int(sunrise_epoc.strftime('%M'))*60
sunset_sec=int(sunset_epoc.strftime('%H'))*60*60+ int(sunset_epoc.strftime('%M'))*60

secPer24Hours = 60*60*24;
sunrise_angle = (360*( sunrise_sec % secPer24Hours )/secPer24Hours)+90
sunset_angle = (360*( sunset_sec % secPer24Hours )/secPer24Hours)+90

radius=100
sunrise_x2=int(math.cos(math.radians(float(sunrise_angle)))*radius)+radius
sunrise_y2=int(math.sin(math.radians(float(sunrise_angle)))*radius)+radius
sunset_x2=int(math.cos(math.radians(float(sunset_angle)))*radius)+radius
sunset_y2=int(math.sin(math.radians(float(sunset_angle)))*radius)+radius

output = output.replace('SUNRISE_X2', str(sunrise_x2))
output = output.replace('SUNRISE_Y2', str(sunrise_y2))
output = output.replace('SUNSET_X2', str(sunset_x2))
output = output.replace('SUNSET_Y2', str(sunset_y2))

# ALL WORK DONE ABOVE -->
codecs.open('sunrise-processed.svg', 'w', encoding='utf-8').write(output)
f.close()
