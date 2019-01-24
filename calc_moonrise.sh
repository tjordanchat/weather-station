#!/bin/bash

export MOONRISE=$(jq .forecast.forecastday[0].astro.moonrise < AP.json)
export MOONSET=$(jq .forecast.forecastday[0].astro.moonset < AP.json)
#echo $MOONRISE $MOONSET
export RISE_SEC=$(echo $MOONRISE | sed 's#[":]# #g' | awk '$3 ~ /PM/ {print (12+$1)*60*60+($2*60)}; $3 ~ /AM/ {print ($1*60*60)+$2*60}')
export SET_SEC=$(echo $MOONSET | sed 's#[":]# #g' | awk '$3 ~ /PM/ {print (12+$1)*60*60+($2*60)}; $3 ~ /AM/ {print ($1*60*60)+$2*60}')

#echo $RISE_SEC $SET_SEC
convert -size 60x60 -strokewidth 5 xc:transparent -fill transparent -stroke black \
        -draw "arc  05,05 30,30 45,270"     draw_arc_partial.gif

