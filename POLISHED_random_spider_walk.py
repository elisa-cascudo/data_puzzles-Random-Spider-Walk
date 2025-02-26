import numpy as np
import random 
import matplotlib.pyplot as plt

#I am going to procede, based off of my solution, to map out the spider's location throughout the simulation
def spider_moves():
    array = np.zeros(2)
    all_simulation_locations = []

    for i in range(239):
        
        theta = random.uniform(0,2*np.pi)
        meters = random.uniform(0,2)
        new_vector = np.array((meters*np.cos(theta) , meters*np.sin(theta)))
        all_simulation_locations.append((meters*np.cos(theta) , meters*np.sin(theta)))
        array = np.add(array, new_vector)

    return array, all_simulation_locations

def monte_carlo(reps):
    count=0

    for i in range(reps):
        array, all_simulation_locations = spider_moves()
        if int(array[0])in range(10,16):
            if int(array[1]) in range(6,11):
                count = count + 1

    probability = count*100/reps
    return probability, all_simulation_locations

probability, all_simulation_locations = monte_carlo(100000)

all_xs, all_ys = zip(*all_simulation_locations)

plt.scatter(all_xs, all_ys)
plt.show()
print(f"The probabilty of the spider being at your palce after 240 minutes is {probability}%")