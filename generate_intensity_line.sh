python intensity_parse.py

#convert svg to png, and rotate 90 degrees for horizontal view
/usr/local/bin/convert -depth 8 -rotate 0 intensity-processed.svg intensity-processed.png

#We optimize the image (necessary for viewing on the kindle)
/usr/local/bin/pngcrush -q -c 0 intensity-processed.png intensity-script-output.png > /dev/null 2>&1
