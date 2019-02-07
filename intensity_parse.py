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
output = codecs.open('rain_timeline.svg', 'r', encoding='utf-8').read()

# ALL WORK DONE BELOW -->

offset=10
width=12
height=15

output = output.replace('WIDTH', str(width))
output = output.replace('HEIGHT', str(height))

for x in range(0, 24):
    xcalc=str(int(offset+(width*x)))
    output = output.replace('XX_'+str(x)+"_", xcalc)
    rain_intens=data["hourly"]["data"][x]["precipIntensity"]
    if rain_intens > 2:
       intensity="100"
    elif rain_intens > 0.3:
        intensity=".75"
    elif rain_intens > 0.1:
        intensity=".50"
    elif rain_intens > 0:
        intensity=".25"
    else:
        intensity="0"

    output = output.replace('FILL_OPAC_'+str(x)+"_", str(intensity))


# ALL WORK DONE ABOVE -->
codecs.open('intensity-processed.svg', 'w', encoding='utf-8').write(output)
f.close()
