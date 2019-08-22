#!/bin/bash
cd /home/pi/ft/socket30003/
sudo ./heatmap.pl -override
sudo mv /tmp/heatmapdata.csv /usr/share/dump1090-mutability/html/heatmapdata.csv
