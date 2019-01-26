#!/usr/bin/python
import math
import sys

def polarToCartesian(centerX, centerY, radius, angleInDegrees):
   angleInRadians = (int(angleInDegrees)-90) * math.pi / 180.0;
   return [
    centerX + (radius * math.cos(angleInRadians)),
    centerY + (radius * math.sin(angleInRadians))]

def describeArc(x, y, radius, startAngle, endAngle):
    start = polarToCartesian(x, y, int(radius), endAngle)
    end = polarToCartesian(x, y, int(radius), startAngle)
    largeArcFlag = "0" if int(endAngle) - int(startAngle) <= 180 else "1"
    return "M "+str(start[0])+" "+str(start[1])+" A "+str(radius)+" "+str(radius)+" 0 "+str(largeArcFlag)+" 0 "+str(end[0])+" "+str(end[1])

# describeArc(x, y, radius, startAngle, endAngle)
x=int(sys.argv[1])
y=int(sys.argv[2])
radius=int(sys.argv[3])
startAngle=int(sys.argv[4])
endAngle=int(sys.argv[5])

print describeArc(x, y, radius, startAngle, endAngle)
