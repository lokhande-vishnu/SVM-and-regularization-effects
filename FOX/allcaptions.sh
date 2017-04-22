#!/bin/bash
# Generates captions for all .ts files and places them in 
# allcaps_final.srt

for zz in $(ls -tr *.ts)
  do
    ffmpeg -f lavfi -i movie=$zz[out+subcc] -map 0:1 /var/tmp/capa5_$zz.srt
    echo $zz >> allcaps_final.srt
    cat /var/tmp/capa5_$zz.srt >> allcaps_final.srt
  done
