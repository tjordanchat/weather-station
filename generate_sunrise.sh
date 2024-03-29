#!/bin/bash

python sunrise_parse.py

alias convert=/opt/homebrew/Cellar/imagemagick/*/bin/convert
#convert svg to png, and rotate 90 degrees for horizontal view
convert -depth 8 -rotate 0 sunrise-processed.svg sunrise-processed.png

#We optimize the image (necessary for viewing on the kindle)
/usr/local/bin/pngcrush -q -c 0 sunrise-processed.png sunrise-script-output.png 2>/dev/null

