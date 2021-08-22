python barometer_parse.py

alias convert=/opt/homebrew/Cellar/imagemagick/*/bin/convert
#convert svg to png, and rotate 90 degrees for horizontal view
convert -depth 8 -rotate 0 barometer-processed.svg barometer-processed.png

#We optimize the image (necessary for viewing on the kindle)
/usr/local/bin/pngcrush -q -c 0 barometer-processed.png barometer-script-output.png > /dev/null 2>&1

