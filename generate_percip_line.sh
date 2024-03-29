python percip_parse.py

alias convert=/opt/homebrew/Cellar/imagemagick/*/bin/convert
#convert svg to png, and rotate 90 degrees for horizontal view
convert -depth 8 -rotate 0 percip-processed.svg percip-processed.png

#We optimize the image (necessary for viewing on the kindle)
/usr/local/bin/pngcrush -q -c 0 percip-processed.png percip-script-output.png > /dev/null 2>&1

