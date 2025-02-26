import numpy as np
import random 

def spider_moves():
    array = np.zeros(2)
    for i in range(239):
        
        theta = random.uniform(0,2*np.pi)
        meters = random.uniform(0,2)
        new_vector = np.array((meters*np.cos(theta) , meters*np.sin(theta)))

        array = np.add(array, new_vector)

    return array

def monte_carlo(reps):
    count=0

    for i in range(reps):
        array = spider_moves()
        if int(array[0])in range(10,16):
            if int(array[1]) in range(6,11):
                count = count + 1

    probability = count*100/reps
    return probability

probability = monte_carlo(100000)

print(f"The probabilty of the spider being at your palce after 240 minutes is {probability}%")