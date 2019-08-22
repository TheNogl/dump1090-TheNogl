import os
import math
w, h = 360, 13;
rang = [[0 for x in range(w)] for y in range(h)]
alt = [[0 for x in range(w)] for y in range(h)]
for filename in sorted(os.listdir('/var/ft/planedata/')):
	if filename.startswith('dump1090'):
		f=open('/var/ft/planedata/'+filename, "r")
		print("Processing: ",filename)
		if f.mode == 'r':
			fl=f.read().splitlines()
			for x in fl:
				x = x.split(',')
				if x[0]!='hex_ident':
					if int(x[1]) >= 0 and int(x[1]) < 1000:
						ind=int(float(x[6]))
						if float(x[7])>rang[0][ind]:
							rang[0][ind]=float(x[7])
							alt[0][ind]=float(x[1])
					elif int(x[1]) >=1000 and int(x[1])<2000:
						ind=int(float(x[6]))
						if float(x[7])>rang[1][ind]:
	                                                rang[1][ind]=float(x[7])
							alt[1][ind]=float(x[1])
					elif int(x[1]) >=2000 and int(x[1])<3000:
                                                ind=int(float(x[6]))
						if float(x[7])>rang[2][ind]:
	                                                rang[2][ind]=float(x[7])
							alt[2][ind]=float(x[1])
					elif int(x[1]) >=3000 and int(x[1])<4000:
                                                ind=int(float(x[6]))
						if float(x[7])>rang[3][ind]:
	                                                rang[3][ind]=float(x[7])
							alt[3][ind]=float(x[1])
					elif int(x[1]) >=4000 and int(x[1])<5000:
                                                ind=int(float(x[6]))
						if float(x[7])>rang[4][ind]:
	                                                rang[4][ind]=float(x[7])
							alt[4][ind]=float(x[1])
                                        elif int(x[1]) >=5000 and int(x[1])<6000:
                                                ind=int(float(x[6]))
						if float(x[7])>rang[5][ind]:
	                                                rang[5][ind]=float(x[7])
							alt[5][ind]=float(x[1])
                                        elif int(x[1]) >=6000 and int(x[1])<7000:
                                                ind=int(float(x[6]))
						if float(x[7])>rang[6][ind]:
	                                                rang[6][ind]=float(x[7])
							alt[6][ind]=float(x[1])
					elif int(x[1]) >=7000 and int(x[1])<8000:
						ind=int(float(x[6]))
						if float(x[7])>rang[7][ind]:
							rang[7][ind]=float(x[7])
							alt[7][ind]=float(x[1])
 					elif int(x[1]) >=8000 and int(x[1])<9000:
 						ind=int(float(x[6]))
						if float(x[7])>rang[8][ind]:
							rang[8][ind]=float(x[7])
							alt[8][ind]=float(x[1])
					elif int(x[1]) >=9000 and int(x[1])<10000:
						ind=int(float(x[6]))
						if float(x[7])>rang[9][ind]:
							rang[9][ind]=float(x[7])
							alt[9][ind]=float(x[1])
					elif int(x[1]) >=10000 and int(x[1])<11000:
						ind=int(float(x[6]))
						if float(x[7])>rang[10][ind]:
							rang[10][ind]=float(x[7])
							alt[10][ind]=float(x[1])
					elif int(x[1]) >=11000 and int(x[1])<12000:
						ind=int(float(x[6]))
						if float(x[7])>rang[11][ind]:
							rang[11][ind]=float(x[7])
							alt[11][ind]=float(x[1])
					elif int(x[1]) >=12000:
                                                ind=int(float(x[6]))
                                                if float(x[7])>rang[12][ind]:
                                                        rang[12][ind]=float(x[7])
                                                        alt[12][ind]=float(x[1])
		f.close()
f = open("/home/pi/ft/data/flighttrackdata/rangeview2.kml","w")
k=0
lat1=48.710527
lon1=15.064188
radiusEarth=6372.7976
lat1=lat1*3.1415926535/180
lon1=lon1*3.1415926535/180
colormap= ["ff135beb", "ff135beb", "ff1383eb", "ff1383eb", "ff13b4eb", "ff13e5eb", "ff13ebc0", "ff13eb8f", "ff13eb5d", "ff13eb2c", "ff2beb13", "ff5ceb13", "ff8eeb13", "ffbfeb13", "ffebe613", "ffebb513", "ffeb8413", "ffeb5213", "ffeb2113", "ffeb1336", "ffeb1367", "ffeb1399", "ffeb13ca", "ffdb13eb", "cc5b13ec", "cc5b13ec"]
f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n  <Document>\n    <name>Paths</name>\n    <description>Example</description>\n")
for i in rang:
	l=0
	f.write("    <Style id=\"track-%d\">\n      <LineStyle>\n        <color>%s</color>\n        <width>2</width>\n      </LineStyle>\n      <PolyStyle>\n         <color>%s</color>\n      </PolyStyle>\n    </Style>\n    <Placemark>\n      <name>%d</name>\n      <description>%d - %d</description>\n      <styleUrl>#track-%d</styleUrl>\n      <LineString>\n        <altitudeMode>absolute</altitudeMode>\n        <coordinates>\n" % (k+1, colormap[k*2], colormap[k*2], k+1, k*1000, (k+1)*1000, k+1))
#	f.write("%d - %d m\n" % (k*1000, (k+1)*1000))
	rang[k][180]=rang[k][179]
	alt[k][180]=alt[k][179]
	for j in rang[k]:
		dist=rang[k][l]/radiusEarth
		bearing=l*3.1415926535/180
		lat2=math.asin(math.sin(lat1)*math.cos(dist) + math.cos(lat1)*math.sin(dist)*math.cos(bearing))
		lon2 = lon1 + math.atan2(math.sin(bearing)*math.sin(dist)*math.cos(lat1), math.cos(dist)-math.sin(lat1)*math.sin(lat2))
		f.write("%.5f,%.5f,%d\n" % (lon2*180/3.1415926535, lat2*180/3.1415926535, int(alt[k][l])))
		l=l+1
	f.write("        </coordinates>\n      </LineString>\n    </Placemark>\n")
#	print(rang[k][178], rang[k][179], rang[k][180], rang[k][181], k)
	k=k+1
f.write("</Document>\n</kml>")
f.close()
