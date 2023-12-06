import pandas as pd
import numpy as np

# Part 1 data
# Time:        44     82     69     81 
# Distance:   202   1076   1138   1458

# Part 2 data

# Time:              44826981
# Distance:   202107611381458

# determine the number of ways you can beat the record in each race; 
# in this example, if you multiply these values together, you get 288 (4 * 8 * 9).

# 0 < time_pressing_button < race_max_time 

race_max_time = 44826981
record_distance = 202107611381458
n_ways_to_beat_record = 0
time_pressing_button = 0


for i in range(0, race_max_time):
    #start race
    time_pressing_button = i 
    remaining_time = race_max_time - time_pressing_button
    if (time_pressing_button * remaining_time) > record_distance:
        n_ways_to_beat_record += 1

print(n_ways_to_beat_record)




