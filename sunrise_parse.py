import math
import tokenize
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

def describeArc(x, y, radius, startAngle, endAngle,arc_rotation):
   start = polarToCartesian(x, y, int(radius), endAngle)
   end = polarToCartesian(x, y, int(radius), startAngle)
   largeArcFlag = "0" if int(endAngle) - int(startAngle) <= 180 else "1" 
   return "M "+str(start[0])+" "+str(start[1])+" A "+str(radius)+" "+str(radius)+" "+str(arc_rotation)+" "+str(largeArcFlag)+" 1 "+str(end[0])+" "+str(end[1])

with open('AP.json') as g:
    ap = json.load(g)

with open('DS.json') as f:
    data = json.load(f)

# Open SVG to process
output = codecs.open('svg_sun_up.svg', 'r', encoding='utf-8').read()

# ALL WORK DONE BELOW -->
moonrise= ap["forecast"]["forecastday"][0]["astro"]["moonrise"]
moonset=ap["forecast"]["forecastday"][0]["astro"]["moonset"]
local_time=ap["location"]["localtime"]

secPer24Hours=60*60*24

mrise_array=moonrise.replace(":"," ")
mset_array=moonset.replace(":"," ")
time_array=local_time.replace(":"," ")

mrise_tokens = mrise_array.split()
mset_tokens = mset_array.split()
time_tokens = time_array.split()

roffset=0
if str(mrise_tokens[2]) == "PM":
   roffset=12

soffset=0
if str(mset_tokens[2]) == "PM":
   soffset=12

mrise_hour=int(mrise_tokens[0])
set_hour=int(mset_tokens[0])
time_hour=int(time_tokens[1])

mrise_minute=int(mrise_tokens[1])
mset_minute=int(mset_tokens[1])
time_minute=int(time_tokens[2])

#rise_sec=(roffset+mrise_hour)*60*60+(mrise_minute*60)
#set_sec=(soffset+mset_hour )*60*60+(mset_minute*60)
time_sec=(time_hour)*60*60+(time_minute*60)

#moonrise_angle=(360*( rise_sec % secPer24Hours)/secPer24Hours)
#moonset_angle= (360*( set_sec % secPer24Hours )/secPer24Hours)

#print("Moonrise: "+str(moonrise_angle))
#print("Moonset: "+str(moonset_angle))
#moon_arc_rotation=(moonrise_angle+moonset_angle)/2

radius=90
dot_radius=90
offset=20
width=12
height=15

#moonrise_x2=int(math.cos(math.radians(float(moonrise_angle)))*radius)
#moonrise_y2=int(math.sin(math.radians(float(moonrise_angle)))*radius)
#moonset_x2=int(math.cos(math.radians(float(moonset_angle)))*radius)
#moonset_y2=int(math.sin(math.radians(float(moonset_angle)))*radius)


#moonrise_arc=describeArc(moonrise_x2, moonrise_y2, radius, moonset_x2, moonset_y2,moon_arc_rotation)

#moonrise_arc="M "+str(moonrise_x2)+" "+str(moonrise_y2)+" A "+str(radius)+" "+str(radius)+" "+str(moon_arc_rotation)+" 0 1 "+str(moonset_x2)+" "+str(moonset_y2)

#output = output.replace('MOONRISE_ARC', str(moonrise_arc))

output = output.replace('WIDTH', str(width))
output = output.replace('HEIGHT', str(height))

sunriseTime=data["daily"]["data"][0]["sunriseTime"]
sunsetTime=data["daily"]["data"][0]["sunsetTime"]

sunrise_epoc = datetime.datetime.fromtimestamp(sunriseTime)
sunset_epoc = datetime.datetime.fromtimestamp(sunsetTime)

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
