#!/usr/bin/python
import math
import sys

def polarToCartesian(centerX, centerY, radius, angleInDegrees):
   angleInRadians = (int(angleInDegrees)-90) * math.pi / 180.0;
   return [
    int(centerX) + (radius * math.cos(angleInRadians)),
    int(centerY) + (radius * math.sin(angleInRadians))]

def describeArc(x, y, radius, startAngle, endAngle):
    start = polarToCartesian(x, y, int(radius), endAngle)
    end = polarToCartesian(x, y, int(radius), startAngle)
    largeArcFlag = "0" if int(endAngle) - int(startAngle) <= 180 else "1"
    return "M "+x+" "+y+" A "+radius+" "+radius+" 0 "+str(largeArcFlag)+" 0 "+str(end[0])+" "+str(end[1])

# describeArc(x, y, radius, startAngle, endAngle)
x=sys.argv[1]
y=sys.argv[2]
radius=sys.argv[3]
startAngle=int(sys.argv[4])
endAngle=int(sys.argv[5])

print describeArc(x, y, radius, startAngle, endAngle)
