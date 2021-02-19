import os
import cgi
import math
import urllib2
from xml.dom import minidom
import time
import datetime
import codecs
import json
import subprocess
from pprint import pprint

def polarToCartesian(centerX, centerY, radius, angleInDegrees):
   angleInRadians = (int(angleInDegrees)-90) * math.pi / 180.0;
   return [ int(centerX) + (radius * math.cos(angleInRadians)),
            int(centerY) + (radius * math.sin(angleInRadians))]

def describeArc(x, y, radius, startAngle, endAngle):
   start = polarToCartesian(x, y, int(radius), endAngle)
   end = polarToCartesian(x, y, int(radius), startAngle)
   largeArcFlag = "0" if int(endAngle) - int(startAngle) <= 180 else "1" 
   return "M "+str(x)+" "+str(y)+" A "+str(radius)+" "+str(radius)+" 0 "+str(largeArcFlag)+" 0 "+str(end[0])+" "+str(end[1])

def getCardinal(angle):
	directions = 8
	degree = 360 / directions
	angle = angle + degree/2
	if angle >= (0 * degree) and angle < (1 * degree):
		return "N"
	if angle >= (1 * degree) and angle < (2 * degree):
		return "NE"
	if angle >= (2 * degree) and angle < (3 * degree):
		return "E"
	if angle >= (3 * degree) and angle < (4 * degree):
		return "SE"
	if angle >= (4 * degree) and angle < (5 * degree):
		return "S"
	if angle >= (5 * degree) and angle < (6 * degree):
		return "SW"
	if angle >= (6 * degree) and angle < (7 * degree):
		return "W"
	if angle >= (7 * degree) and angle < (8 * degree):
		return "NW"
	return "N"

with open('DS.json') as f:
    data = json.load(f)

# Open SVG to process
output = codecs.open('template.svg', 'r', encoding='utf-8').read()

feels_like=int(data["currently"]["apparentTemperature"])

wind_degree=int(data["currently"]["windBearing"])
wind_dir_url="assets/W_IND_"+getCardinal(wind_degree)+".jpg"

status=cgi.escape(data["currently"]["summary"] )
output = output.replace('STATUS',status) 

#need to map icons
image = data["currently"]["icon"]
image_url = 'assets/' + str(image) + '.png'
output = output.replace('ICON_ONE',image_url)

# Do calculations
pressure=data["currently"]["pressure"]
fpressure=data["hourly"]["data"][6]["pressure"]
if pressure > fpressure:
    tending="Cloud"
else:
    tending="Sun"
# 33.864

bar=int((float(pressure) - 982)/17)
bar_url = 'assets/'+tending+"_" + str(bar) + '.jpg'
output = output.replace('ICON_BAR', bar_url)

output = output.replace('WIND_DIR_ICON', wind_dir_url)
output = output.replace('FEELS_LIKE', str(int(feels_like)))

rain_intens=float(data["currently"]["precipIntensity"])
if rain_intens > 2:
    intensity="VIOLENT"
elif rain_intens > 0.3:
    intensity="HEAVY"
elif rain_intens > 0.1:
    intensity="MODERATE"
elif rain_intens > 0.02:
    intensity="LIGHT"
else:
    intensity="NA"
rain_intens_icon="assets/INTEN_"+intensity+".jpg"
output = output.replace('INTENSITY',rain_intens_icon)

dew_point=int(data["currently"]["dewPoint"])
if dew_point < 55:
    dew_value="0"
elif dew_point < 60:
    dew_value="1"
elif dew_point < 65:
    dew_value="2"
elif dew_point < 70:
    dew_value="3"
elif dew_point < 75:
    dew_value="4"
else:
    dew_value="5"
dew_point_icon="assets/Dew_Point_"+dew_value+".jpg"
output = output.replace('DEW_POINT_ICON',dew_point_icon)


cloud_cover=data["currently"]["cloudCover"]
if cloud_cover == 0:
    cloud_cov="0"
elif cloud_cover <= .1:
    cloud_cov="1"
elif cloud_cover <= .25:
    cloud_cov="23"
elif cloud_cover <= .45:
    cloud_cov="4"
elif cloud_cover <= .55:
    cloud_cov="5"
elif cloud_cover <= .65:
    cloud_cov="6"
elif cloud_cover <= .85:
    cloud_cov="78"
else:
    cloud_cov="9"

cloud_cov_icon="assets/COVERAGE_"+cloud_cov+".jpg"
output = output.replace('CLOUD_COV_ICON',cloud_cov_icon)


precip=0.0
for x in range(0):
    i=float(data["hourly"]["data"][x]["precipProbability"])
    if i > precip:
       precip=i

precip=data["currently"]["precipProbability"]

if precip > .87:
  rain="100"
elif precip > .7:
  rain="75"
elif precip > .37:
  rain="50"
elif precip > .17:
  rain="25"
else:
  rain="0"

precip_icon="assets/Rain_"+rain+".jpg"
output = output.replace('PRECIPER',precip_icon)
output = output.replace('PRECIP_TXT',str(int(precip*100)))

# Insert icons and temperatures

summary=cgi.escape(data["hourly"]["summary"])
output = output.replace('SUMMARY',summary)
wind=str(int(data["currently"]["windSpeed"]+.5))

output = output.replace('WIND',wind)
anchor_x="85"
if int(wind) < 10:
    anchor_x="65"
output = output.replace('ANCHOR_150',anchor_x)

if rain_intens > 0:
  parcip_type=data["currently"]["precipType"]
else:
	parcip_type="NA"
if parcip_type == "rain":
	parcip_type_icon="assets/RainDrop.png"
elif parcip_type == "snow":
	parcip_type_icon="assets/SnowFlake.png"
elif parcip_type == "hail":
	parcip_type_icon="assets/Hail.png"
elif parcip_type == "sleet":
	parcip_type_icon="assets/Sleet.png"
else:
	parcip_type_icon="assets/catus.png"
output = output.replace('__PARCIP_TYPE_ICON__',parcip_type_icon)

visibility=data["currently"]["visibility"]
if visibility >= 10:
	visibility_icon="assets/VISIBILITY_0.jpg"
elif visibility >= 9:
	visibility_icon="assets/VISIBILITY_1.jpg"
elif visibility >= 8:
	visibility_icon="assets/VISIBILITY_2.jpg"
elif visibility >= 7:
	visibility_icon="assets/VISIBILITY_3.jpg"
elif visibility >= 6:
	visibility_icon="assets/VISIBILITY_4.jpg"
elif visibility >= 5:
	visibility_icon="assets/VISIBILITY_5.jpg"
elif visibility >= 3:
	visibility_icon="assets/VISIBILITY_6.jpg"
elif visibility >= 1:
	visibility_icon="assets/VISIBILITY_7.jpg"
elif visibility >= .5:
	visibility_icon="assets/VISIBILITY_8.jpg"
else:
	visibility_icon="assets/VISIBILITY_9.jpg"
output = output.replace('__VISIBILITY_MARK__',visibility_icon)

now=data["currently"]["time"]
concisedate= datetime.datetime.fromtimestamp(now).strftime('%b %d')
concisetime= datetime.datetime.fromtimestamp(now).strftime('%H:%M')
output = output.replace('TODAY',concisedate)
output = output.replace('HOUR', concisetime)

output = output.replace('CITY',"New York")

fhumid=int(float(data["hourly"]["data"][4]["humidity"])*100)
humidity=int(float(data["currently"]["humidity"])*100)

if humidity > fhumid:
   output = output.replace('HUPDOWN','assets/DOWN.jpg')
else:
   output = output.replace('HUPDOWN','assets/UP.jpg')

output = output.replace('HUMID',str(int(humidity)))
temp=int(data["currently"]["temperature"])
output = output.replace('HIGH_ONE',str(int(temp)))  
speed=int(data["currently"]["windSpeed"]) 
output = output.replace('SPEED',str(int(round(float(speed))))) 

ftemp=data["hourly"]["data"][2]["temperature"]
if temp > ftemp:
   updown="assets/DOWN.jpg"
else:
   updown="assets/UP.jpg"

output = output.replace('UPDOWN',updown)

# FORECAST 

output = output.replace('ICON_01', 'assets/' + str(data["daily"]["data"][0]["icon"]) + '.png') 
output = output.replace('ICON_02', 'assets/' + str(data["daily"]["data"][1]["icon"]) + '.png') 
output = output.replace('ICON_03', 'assets/' + str(data["daily"]["data"][2]["icon"]) + '.png') 
output = output.replace('ICON_04', 'assets/' + str(data["daily"]["data"][3]["icon"]) + '.png')

uvIndex=data["currently"]["uvIndex"]
if uvIndex == 10:
    uvIndex='X'
output = output.replace('UVINDEX', str(uvIndex))

date_epoch=data["daily"]["data"][0]["time"] 
concise_day= datetime.datetime.fromtimestamp(date_epoch).strftime('%a')
output = output.replace('FORECAST_DAY_01', concise_day)
high=str(int(data["daily"]["data"][0]["temperatureHigh"]))
low=str(int(data["daily"]["data"][0]["temperatureLow"]))
output = output.replace('FORECAST_HILO_01', high +'/' + low)

date_epoch=data["daily"]["data"][1]["time"] 
concise_day= datetime.datetime.fromtimestamp(date_epoch).strftime('%a')
high=str(int(data["daily"]["data"][1]["temperatureHigh"]))
low=str(int(data["daily"]["data"][1]["temperatureLow"]))
output = output.replace('FORECAST_DAY_02', concise_day)
output = output.replace('FORECAST_HILO_02', high +'/' + low)

date_epoch=data["daily"]["data"][2]["time"] 
concise_day= datetime.datetime.fromtimestamp(date_epoch).strftime('%a')
high=str(int(data["daily"]["data"][2]["temperatureHigh"]))
low=str(int(data["daily"]["data"][2]["temperatureLow"]))
output = output.replace('FORECAST_DAY_03', concise_day)
output = output.replace('FORECAST_HILO_03', high +'/' + low)

date_epoch=data["daily"]["data"][3]["time"] 
concise_day= datetime.datetime.fromtimestamp(date_epoch).strftime('%a')
high=str(int(data["daily"]["data"][3]["temperatureHigh"]))
low=str(int(data["daily"]["data"][3]["temperatureLow"]))
output = output.replace('FORECAST_DAY_04', concise_day)
output = output.replace('FORECAST_HILO_04', high +'/' + low) # Write 


codecs.open('weather-processed.svg', 'w', encoding='utf-8').write(output)

f.close()
