import math
import tokenize
import urllib2
from xml.dom import minidom
import time
from datetime import datetime
import codecs
import json
from pprint import pprint

def polarToCartesian(centerX, centerY, radius, angleInDegrees):
   angleInRadians = (int(angleInDegrees)-90) * math.pi / 180.0;
   return [ int(centerX) + (radius * math.cos(angleInRadians)), int(centerY) + (radius * math.sin(angleInRadians))]

def describeArc(x, y, radius, startAngle, endAngle,arc_rotation):
   start = polarToCartesian(x, y, int(radius), endAngle)
   end = polarToCartesian(x, y, int(radius), startAngle)
   largeArcFlag = "0" if int(endAngle) - int(startAngle) <= 180 else "1" 
   return "M "+str(start[0])+" "+str(start[1])+" A "+str(radius)+" "+str(radius)+" "+str(arc_rotation)+" "+str(largeArcFlag)+" 1 "+str(end[0])+" "+str(end[1])

with open('DS.json') as f:
    data = json.load(f)

# Open SVG to process
output = codecs.open('svg_sun_up.svg', 'r', encoding='utf-8').read()

# ALL WORK DONE BELOW -->
now = datetime.now()
local_time = now.strftime("%H %M")
time_tokens=local_time.split()

secPer24Hours=60*60*24

roffset=0
soffset=0

time_hour=int(time_tokens[0])

time_minute=int(time_tokens[1])

time_sec=(time_hour)*60*60+(time_minute*60)+900

radius=90
dot_radius=90
offset=20
width=12
height=15

output = output.replace('WIDTH', str(width))
output = output.replace('HEIGHT', str(height))

sunriseTime=data["daily"]["data"][0]["sunriseTime"]
sunsetTime=data["daily"]["data"][0]["sunsetTime"]

sunrise_epoc = datetime.fromtimestamp(sunriseTime)
sunset_epoc = datetime.fromtimestamp(sunsetTime)

sunrise_sec=int(sunrise_epoc.strftime('%H'))*60*60+ int(sunrise_epoc.strftime('%M'))*60
sunset_sec=int(sunset_epoc.strftime('%H'))*60*60+ int(sunset_epoc.strftime('%M'))*60

sunrise_angle = ((360*( sunrise_sec % secPer24Hours )/secPer24Hours)+90)%360
sunset_angle =  ((360*( sunset_sec % secPer24Hours )/secPer24Hours)+90)%360
time_angle   =  ((360*( time_sec   % secPer24Hours )/secPer24Hours)+90)%360

print("Sunrise: "+str(sunrise_angle))
print("Sunset: "+str(sunset_angle))

sunrise_x2=int(math.cos(math.radians(float(sunrise_angle)))*radius)+radius+offset
sunrise_y2=int(math.sin(math.radians(float(sunrise_angle)))*radius)+radius+offset
sunset_x2=int(math.cos(math.radians(float(sunset_angle)))*radius)+radius+offset
sunset_y2=int(math.sin(math.radians(float(sunset_angle)))*radius)+radius+offset
time_x2  =int(math.cos(math.radians(float(time_angle)))*dot_radius)+dot_radius+offset
time_y2  =int(math.sin(math.radians(float(time_angle)))*dot_radius)+dot_radius+offset

output = output.replace('SUNRISE_X2', str(sunrise_x2))
output = output.replace('SUNRISE_Y2', str(sunrise_y2))
output = output.replace('SUNSET_X2', str(sunset_x2))
output = output.replace('SUNSET_Y2', str(sunset_y2))
output = output.replace('TIME_X2', str(time_x2))
output = output.replace('TIME_Y2', str(time_y2))

# ALL WORK DONE ABOVE -->
codecs.open('sunrise-processed.svg', 'w', encoding='utf-8').write(output)
f.close()
