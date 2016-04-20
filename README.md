# Dump1090-mutability Debian/Raspbian packages with heatmap & rangeview
[![Build Status](https://travis-ci.org/mutability/dump1090.svg?branch=master)](https://travis-ci.org/mutability/dump1090)

[Dump1090-mutability](https://github.com/mutability/dump1090) is Oliver Jowett's fork of [MalcolmRobb's version of dump1090](https://github.com/MalcolmRobb/dump1090)
that adds new functionality and is designed to be built as
a Debian/Raspbian package.
This fork adds a heatmap and rangeview to it.

This version is licensed under the GPL (v2 or later).
See the file COPYING for details.

# Dump1090-mutability features

* 2.4MHz "oversampling" support
* doesn't run as root
* supports FlightAware-TSV-format connections directly (same as the FlightAware version - no faup1090 needed)
* can start from init.d, with detailed config via debconf or `/etc/default/dump1090-mutability`
* can serve the virtual radar map via an external webserver (lighttpd integration included by default)
* map view uses receiver lat/long given to dump1090 automatically
* somewhat cleaned-up network code
* tries to do things "the debian way" when it comes to config, package structure, etc
* probably a bunch of other things I've forgotten..

# Extra heatmap & rangeview features

* display a csv heatmap file (a sample heatmap is included).
* adjust the opacity, intensity and radius of the heatmap from a movable panel.
* load a heatmap from the dump1090 web directory or from the heatmap panel in the browser.
* display a KML range/altitude file (a link to a sample rangeview file is included)..
* display distance range rings around the antenna if the ability to toggle it.
* provide moveable legends for the altitude colors and range rings.
* toggle plane colors between Altitude colors and adb-s/mlat position colors.
* toggle the heatmap and the range/altitude view on and off (including their panel and legends).

# Live view

Watch my dump1090 fork with heatmap and rangeview in the Google cloud: http://130.211.186.77/dump1090/gmap.html
(This dump1090 runs on a 60-day free trail that is available until 20 june 2016)

# Screenshots and video

Heatmap
[![Dump1090 Heatmap](https://dl.dropboxusercontent.com/u/17865731/dump1090-20150916/heatmapexample16.png)](https://dl.dropboxusercontent.com/u/17865731/dump1090-20150916/heatmapexample16.png)

Rangeview
[![Dump1090 rangeview](https://dl.dropboxusercontent.com/u/17865731/dump1090-20150916/rangeviewexample16.png)](https://dl.dropboxusercontent.com/u/17865731/dump1090-20150916/rangeviewexample16.png)

Youtube video:
[![Dump1090 rangeview](https://dl.dropboxusercontent.com/u/17865731/dump1090-20150916/youtube16.png)](https://www.youtube.com/watch?v=Qz4XSFRjLTI)

# Manual installation

To build it from source first install these packages:
````
apt-get update && apt-get install -y apt-utils build-essential ca-certificates cron curl debhelper dialog dpkg-dev git librtlsdr-dev libusb-1.0-0-dev lighttpd netcat net-tools pkg-config python2.7 wget 
````

You will need a librtlsdr0 package for Raspbian.
There is no standard build of this.
Oliver Jowett has built suitable packages that are available from 
[this release page](https://github.com/mutability/librtlsdr/releases)  
Install these rtl-sdr  packages with dpkg:   
````
$ wget https://github.com/mutability/librtlsdr/releases/download/v0.5.4_git-1/librtlsdr0_0.5.4.git-1_armhf.deb
$ wget https://github.com/mutability/librtlsdr/releases/download/v0.5.4_git-1/librtlsdr-dev_0.5.4.git-1_armhf.deb
$ wget https://github.com/mutability/librtlsdr/releases/download/v0.5.4_git-1/rtl-sdr_0.5.4.git-1_armhf.deb
$ sudo dpkg -i librtlsdr0_0.5.4.git-1_armhf.deb
$ sudo dpkg -i librtlsdr-dev_0.5.4.git-1_armhf.deb
$ sudo dpkg -i rtl-sdr_0.5.4.git-1_armhf.deb
````

On X86 you should install these rtl-sdr packages:   
````
apt-get update && apt-get install -y librtlsdr0 rtl-sdr 
````

Build dump1090 from source:
````
$ git clone https://github.com/tedsluis/dump1090.git
$ cd dump1090
$ dpkg-buildpackage -b
````

Install dump1090:
````
$ cd ..
$ dpkg -i dump1090-mutability_1.15~dev_armhf.deb
````

Configure the web server:
````
$ sudo lighty-enable-mod dump1090
$ sudo service lighttpd force-reload
````
This uses a configuration file installed by the package at `/etc/lighttpd/conf-available/89-dump1090.conf`.   
It makes the map view available at http://<pi address>/dump1090/   

## Step by step instructions

A step by step installation instruction for Raspbian is available at: 
[http://discussions.flightaware.com/ads-b-flight-tracking-f21/heatmap-range-altitude-view-for-dump1090-mutability-v1-15-t35844.html](http://discussions.flightaware.com/ads-b-flight-tracking-f21/heatmap-range-altitude-view-for-dump1090-mutability-v1-15-t35844.html)   

## Dump1090 in a docker container
  
A dump1090 installation in a Docker container is also possible. Follow the instructions for X86_64/AMD64 and ARM(Raspbian) at [github.com/tedsluis/docker-dump1090](https://github.com/tedsluis/docker-dump1090) or [hub.docker.com/r/tedsluis/dump1090-mutability](https://hub.docker.com/r/tedsluis/dump1090-mutability)   

# Configuration

By default it'll only ask you whether to start automatically and assume sensible defaults for everything else.
Notable defaults that are perhaps not what you'd first expect:

* All network ports are bound to the localhost interface only.
  If you need remote access to the ADS-B data ports, you will want to change this to bind to the wildcard address.
* The internal HTTP server is disabled. I recommend using an external webserver (see below).
  You can reconfigure to enable the internal one if you don't want to use an external one.

To reconfigure, either use `dpkg-reconfigure dump1090-mutability` or edit `/etc/default/dump1090-mutability`. Both should be self-explanatory.

## Logging

The default configuration logs to `/var/log/dump1090-mutability.log` (this can be reconfigured).
The only real logging other than any startup problems is hourly stats.
There is a logrotate configuration installed by the package at `/etc/logrotate.d/dump1090-mutability` that will rotate that logfile weekly.

# Bug reports, feedback etc

Please use the [github issues page](https://github.com/tedsluis/dump1090/issues) to report any problems.

Ted Sluis  
ted.sluis@gmail.com  
https://github.com/tedsluis  
https://hub.docker.com/r/tedsluis  
[https://www.youtube.com/tedsluis](https://www.youtube.com/channel/UCnR4rVCm_8gCjY_m3t1ExgA)   
http://flightaware.com/adsb/stats/user/tedsluis#stats-6731  
