import math

def distance(lon1, lat1, lon2, lat2):
	R = 6371e3
	phi1 = math.radians(lat1)
	phi2 = math.radians(lat2)
	deltaphi = math.radians(lat2 - lat1)
	deltalambda = math.radians(lon2 - lon1)
	
	a = math.sin(deltaphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * (math.sin(deltalambda / 2) ** 2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
	
	return R * c