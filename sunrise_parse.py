import math
import urllib2
from xml.dom import minidom
import time
import datetime
import codecs
import json
from pprint import pprint

def polarToCartesian(centerX, centerY, radius, angleInDegrees):
   angleInRadians = (int(angleInDegrees)-90) * math.pi / 180.0;
   return [ int(centerX) + (radius * math.cos(angleInRadians)), int(centerY) + (radius * math.sin(angleInRadians))]

def describeArc(x, y, radius, startAngle, endAngle):
   start = polarToCartesian(x, y, int(radius), endAngle)
   end = polarToCartesian(x, y, int(radius), startAngle)
   largeArcFlag = "0" if int(endAngle) - int(startAngle) <= 180 else "1" 
   return "M "+str(x)+" "+str(y)+" A "+str(radius)+" "+str(radius)+" 0 "+str(largeArcFlag)+" 0 "+str(end[0])+" "+str(end[1])

with open('AP.json') as g:
    ap = json.load(g)

with open('DS.json') as f:
    data = json.load(f)

# Open SVG to process
output = codecs.open('svg_sun_up.svg', 'r', encoding='utf-8').read()

# ALL WORK DONE BELOW -->
moonrise= ap["forecast"]["forecastday"][0]["astro"]["moonrise"]
moonset=ap["forecast"]["forecastday"][0]["astro"]["moonset"]

secPer24Hours=60*60*24

mrise_array=moonrise.replace(":"," ")
mset_array=moonset.replace(":"," ")

roffset=0
if mrise_array[2] == "PM":
   roffset=12

soffset=0
if mset_array[2] == "PM":
   soffset=12

mrise_hour=int(mrise_array[0])
mset_hour=int(mset_array[0])

mrise_minute=int(mrise_array[1])
mset_minute=int(mset_array[1])

rise_sec=(roffset+mrise_hour)*60*60+(mrise_minute*60)
set_sec=(soffset+mset_hour)*60*60+(mset_minute*60)

moonrise_angle=360*( rise_sec % secPer24Hours)/secPer24Hours-90
moonset_angle=(360*( set_sec % secPer24Hours )/secPer24Hours)-90

msize=15
moonrise_arc=describeArc(20, 185, msize, moonrise_angle, moonset_angle)

output = output.replace('MOONRISE_ARC', str(moonrise_arc))

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
