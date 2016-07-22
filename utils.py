import os

PLOTFILE = 'plotdata.txt'
CLEAR_PLOTFILE = True  	#When init - delete previous plotfil
OUTPUTDIR = 'script_out'

def initUtils():
	if(CLEAR_PLOTFILE):
		if os.path.isfile(PLOTFILE):
			os.remove(PLOTFILE)
	with open(PLOTFILE, 'w') as plotfile:
		plotfile.write('#NanoClockDiff \t\t GPSClockDiff \n#\n')


def log_diff(nanoclockDiff, gpsDiff):
	with open(PLOTFILE, 'a') as plotfile:
		plotfile.write(str(nanoclockDiff)+'\t\t'+str(gpsDiff)+'\n')


## Calculate Distance
#
#  From: http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r




initUtils()