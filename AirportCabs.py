import numpy as np

taxi = np.genfromtxt('nyc_taxisProject.csv', delimiter = ',', skip_header=True)

# speed in km/hr
speed = (taxi[:, 7]) * 1.60934/(taxi[:,8]/3600)
print(speed)

# mean speed of all the rides
mean_speed = speed.mean()
print(mean_speed)

# number of rides in February
feb_rides = taxi[taxi[:, 1] == 2, 1]
print(feb_rides.shape[0])

# number of rides with tips more than $50
tip_rides = taxi[taxi[:, -3] > 50, -3].shape[0]
print(tip_rides)

# number of rides where drop-off was at JFK
# drop-off location code for JFK is 2
JFK_drop = taxi[taxi[:, 6] == 2, 6].shape[0]
print(JFK_drop)