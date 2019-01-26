#!/bin/bash

export MOONRISE=$(jq .forecast.forecastday[0].astro.moonrise < AP.json)
export MOONSET=$(jq .forecast.forecastday[0].astro.moonset < AP.json)
#echo $MOONRISE $MOONSET
export RISE_SEC=$(echo $MOONRISE | sed 's#[":]# #g' | awk '$3 ~ /PM/ {print (12+$1)*60*60+($2*60)}; $3 ~ /AM/ {print ($1*60*60)+$2*60}')
export SET_SEC=$(echo $MOONSET | sed 's#[":]# #g' | awk '$3 ~ /PM/ {print (12+$1)*60*60+($2*60)}; $3 ~ /AM/ {print ($1*60*60)+$2*60}')

#echo $RISE_SEC $SET_SEC

export secPer24Hours=$(( 60*60*24 ))
#echo $secPer24Hours

export moonrise_angle=$(( (360*( $RISE_SEC % $secPer24Hours )/$secPer24Hours)+90 ))
export moonset_angle=$(( (360*( $SET_SEC % $secPer24Hours )/$secPer24Hours)+90 ))

echo $( ./calc-arc.py 100 100 50 $moonrise_angle $moonset_angle )
