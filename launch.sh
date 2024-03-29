#!/bin/sh
set -xv

PATH=$PATH:/opt/homebrew/bin

echo "##########################################################################"
cd "$(dirname "$0")"

DARK_KEY=$(cat pass.yml | /usr/local/bin/yq e .darksky.key -)
DARK_LAT=$(cat pass.yml | /usr/local/bin/yq e .darksky.coord.lat -)
DARK_LONG=$(cat pass.yml | /usr/local/bin/yq e .darksky.coord.long -)
APIX_KEY=$(cat pass.yml | /usr/local/bin/yq e .apixu.key - )
APIX_ZIP=$(cat pass.yml | /usr/local/bin/yq e .apixu.zip -)

curl https://api.darksky.net/forecast/$DARK_KEY/$DARK_LAT,$DARK_LONG | /usr/local/bin/jq . > DS.json

curl -k "http://api.apixu.com/v1/forecast.json?key=$APIX_KEY&q=$APIX_ZIP&days=5"  | /usr/local/bin/jq . > AP.json

MOON_PHASE=$(cat DS.json | /usr/local/bin/jq .daily.data[0].moonPhase )
#curl -k https://api.usno.navy.mil/imagery/moon.png > moon.png

rm -f namfntsfcwbg.gif
wget https://www.wpc.ncep.noaa.gov/sfc/namfntsfcwbg.gif
rm -f ECVS.JPG
#rm -f ./news/*
wget https://www.goes.noaa.gov/GIFS/ECVS.JPG
./generate_percip_line.sh
./generate_temp_line.sh
./generate_sunrise.sh
./generate_humid_line.sh
./generate_wind_line.sh
./generate_intensity_line.sh
./generate_barometer_line.sh
./newsapi.sh
#./calc_moonrise.sh
sed "s/__THIS_IS_THE_MOON_PHASE__/$MOON_PHASE/g" < PRE-moon.html > moon.html
'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' --headless --disable-gpu --screenshot=moon.png moon.html

#Parse Weather and replace placeholder text in the svg template file
python parse_weather.py

rm -f weather-processed.png

#convert svg to png, and rotate 90 degrees for horizontal view
alias convert=/opt/homebrew/Cellar/imagemagick/*/bin/convert
convert -depth 8 -quality 100 -rotate 90 weather-processed.svg weather-processed.png
convert -depth 8 -quality 100 weather-processed.svg weather-processed2.png
convert -depth 8 -quality 100 -rotate 90 namfntsfcwbg.gif namfntsfcwbg90.gif
convert -depth 8 -quality 100 -rotate 90 ECVS.JPG ECVS90.JPG

#We optimize the image (necessary for viewing on the kindle)
/usr/local/bin/pngcrush -q -c 0 weather-processed.png weather-script-output.png
/usr/local/bin/pngcrush -q -c 0 weather-processed2.png weather-script-output2.png

