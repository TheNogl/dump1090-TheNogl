// -*- mode: javascript; indent-tabs-mode: nil; c-basic-offset: 8 -*-
"use strict";

//
// 'toverfield' added another legend for the range circles and toggle controls for both legends. He also made the range circles easier to configure.
//

var myMarker = null;
var CirclesArray = [];

function getAltitudeZoneColors(NumberOfZones) {
    var html = '';

	if (!ShowAircraftColorLegend)
	    return html;

	if (!ShowAltitudesByColor){
		html='<li class="color" style="color:black; background-color: #80ff80;">ADS-B Positions</li>' +
			 '<li class="color" style="color:black; background-color: #8080ff;">MLAT Positions</li>';
		return html;
	}

	var unittype = ' ft';
	if (Metric) unittype = ' m';

	// Number of Meters or feet per zone
	var MaximumAltitude = MaxAltitudeFeet
	if (Metric) MaximumAltitude = MaxAltitudeMeters;
	var zone = Math.round(MaximumAltitude / NumberOfAltitudeZones);

	// create zone color for every altitude zone
	for (var altitude_zone = 0; altitude_zone < NumberOfZones; ++altitude_zone){
		var altitude = altitude_zone * zone;	

		// calculate low and high zone border
		var low_altitude_zone_border = Math.round(altitude);
		var high_altitude_zone_border = Math.round(((altitude_zone + 1) * zone)) - 1;

		// color
		var s = ColorByAlt.air.s;
		var l = ColorByAlt.air.l;

		if (Metric) altitude = Math.round(altitude * 3.2828);

		// find the pair of points the current altitude lies between,
		// and interpolate the hue between those points
		var hpoints = ColorByAlt.air.h;
		var h = hpoints[0].val;
		for (var i = hpoints.length-1; i >= 0; --i) {
			if (altitude > hpoints[i].alt) {
				if (i == hpoints.length-1) {
					h = hpoints[i].val;
				} else {
					h = hpoints[i].val + (hpoints[i+1].val - hpoints[i].val) * (altitude - hpoints[i].alt) / (hpoints[i+1].alt - hpoints[i].alt)
				} 
				break;
			}
		}

		if (h < 0) {
			h = (h % 360) + 360;
		} else if (h >= 360) {
			h = h % 360;
		}

		if (s < 5) s = 5;
		else if (s > 95) s = 95;

		if (l < 5) l = 5;
		else if (l > 95) l = 95;

		var zone_color = 'hsl(' + h.toFixed(0) + ',' + s.toFixed(0) + '%,' + l.toFixed(0) + '%)';

		// Create HTML code
		html=html+'<li class="color" style="background-color:'+zone_color+';">'+low_altitude_zone_border+'-'+high_altitude_zone_border+unittype+'</li>';
	}

	return html; 
}

function getRangeRingsLegend() {
    var html="";

    if (!ShowSiteCircles) return html;
    if (!ShowSiteCirclesLegend) return html;

    var unittype = ' nm';
    if (Metric) unittype = ' km';

    // Create HTML code

    // Make a legend heading
    // html='<li class="color" style="color:white; background-color:green;">Range Rings</li>';
    for (var i=0;i<SiteCircle.length;i++) {
        html=html+'<li class="color" style="color:white; background-color:'+SiteCircle[i].color+';">'+SiteCircle[i].distance+unittype+'</li>';
    }

    return html;
}

function refresh_colored_altitude_zones() {
    document.getElementById('draggable-altitude-legend').innerHTML=getAltitudeZoneColors(NumberOfAltitudeZones);
}

function refresh_range_legend() {
    document.getElementById('draggable-range-legend').innerHTML=getRangeRingsLegend();
}

function toggleRings() {
    ShowSiteCircles = !ShowSiteCircles;
    var e = document.getElementById("draggable-range-legend");
    if (ShowSiteCircles) {
         e.style.display = 'block';
    } else {
         e.style.display = 'none';
    }
    if (SitePosition) refreshCircles(myMarker);
}

function toggleColors() {
    ShowAltitudesByColor = !ShowAltitudesByColor;
    refresh_colored_altitude_zones();
}

function refreshCircles(marker) {
    for (var i=0; i < SiteCircle.length; i++) 
        if (ShowSiteCircles) {
            if (!CirclesArray[i])
                CirclesArray[i] = drawCircle(marker, SiteCircle[i].distance, SiteCircle[i].strokeweight, SiteCircle[i].color);
        } else {
            if (CirclesArray[i]) {
                CirclesArray[i].setMap(null);
                CirclesArray[i] = null;
            }
        }
    refresh_range_legend();
}

