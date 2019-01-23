#!/bin/sh

cd "$(dirname "$0")"

curl https://api.darksky.net/forecast/d139fe35e51438a0bd7b376b8b40943f/40.7,-74 | /usr/local/bin/jq . > DS.json

curl -k "http://api.apixu.com/v1/forecast.json?key=4a3bb70d7f614c238f6192225190301&q=10001&days=5"  | /usr/local/bin/jq . > AP.json

curl -k https://api.usno.navy.mil/imagery/moon.png > phase.png

export PRECIP=$( cat DS.json  | /usr/local/bin/jq ".currently.precipProbability" ) 2>/dev/null

export RAIN

if echo "$PRECIP > .17" | bc >/dev/null
	then
	RAIN=25
	elif "$PRECIP > .37" | bc >/dev/null
		then
	RAIN=50
	elif "$PRECIP > .63" | bc >/dev/null
		then
	RAIN=75
	elif "$PRECIP > .87.5" | bc >/dev/null
		then
		RAIN=100
fi

./generate_percip_line.sh
./generate_temp_line.sh
./generate_sunrise.sh
./generate_humid_line.sh
./generate_wind_line.sh

cp -f assets/Rain_$RAIN.jpg PRECIP.jpg

export NOW=$( cat DS.json 2>/dev/null| /usr/local/bin/jq .hourly.data[0].pressure )
export SOON=$( cat DS.json 2>/dev/null| /usr/local/bin/jq .hourly.data[1].pressure )

export TNOW=$( cat DS.json 2>/dev/null| /usr/local/bin/jq .hourly.data[0].temperature )
export TSOON=$( cat DS.json 2>/dev/null| /usr/local/bin/jq .hourly.data[1].temperature )

if echo "$NOW > $SOON" | bc >/dev/null
	then
	DIR=Minus
	else 
		DIR=Plus
		fi
		BAR=$( echo "( $NOW - 969 ) / 20.4" | bc )

		cp assets/${DIR}_$BAR.jpg BAR.jpg

if echo "$TNOW > $TSOON" | bc >/dev/null
then
	echo "▲" > TDIR.txt
else
	echo "▼" > TDIR.txt
fi
	

cat DS.json | /usr/local/bin/jq .minutely.summary | sed 's/"//g' > SUMMARY.txt
export SPEED=$(cat DS.json | /usr/local/bin/jq .hourly.data[0].windSpeed | sed 's/"//g' )
echo "($SPEED + .5 )/1" | bc > WIND.txt

#Parse Weather and replace placeholder text in the svg template file
python parse_weather.py

#convert svg to png, and rotate 90 degrees for horizontal view
sudo /usr/local/bin/convert -depth 8 -rotate 90 weather-processed.svg weather-processed.png
sudo /usr/local/bin/convert -depth 8 weather-processed.svg weather-processed2.png

#We optimize the image (necessary for viewing on the kindle)
sudo /usr/local/bin/pngcrush -q -c 0 weather-processed.png weather-script-output.png > /dev/null 2>&1
sudo /usr/local/bin/pngcrush -q -c 0 weather-processed2.png weather-script-output2.png > /dev/null 2>&1

