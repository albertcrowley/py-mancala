#!/bin/bash

while [ 1 ]
do
  killall feh
  ID=$(ls  figures | cut -d '-' -f 2 | cut -d '.' -f 1 | sort -n | tail -1 )
  feh figures/improvement-${ID}.png &
  sleep 20
 done

