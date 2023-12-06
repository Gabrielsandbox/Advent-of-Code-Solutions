import numpy as np
import pandas as pd

# z           x            y   
# 1280158874  0            45923291
# 0           1431836695   234754481

# z = destination range start (soil map)
# x = source range start (seed map)
# y = range length (map range)

# select seed                       # 4501055
# if seed >= x and seed <= x + y:   # 4501055 >= 0 and 4501055 <= 45923291
# seed - x = seed_index             # 4501055 - 0 = 4501055
# z + seed_index = soil             # 1280158874 + 4501055 = 1284669939

# check every map for a given code
# if code is in map, return the corresponding value

seeds = [1132132257, 323430997, 2043754183, 4501055, 2539071613, 1059028389, 1695770806, 60470169, 2220296232, 
         251415938, 1673679740, 6063698, 962820135, 133182317, 262615889, 327780505, 3602765034, 194858721, 2147281339, 37466509]


soil = np.zeros(len(seeds))
fertilizer = np.zeros(len(seeds))
water = np.zeros(len(seeds))
light = np.zeros(len(seeds))
temperature = np.zeros(len(seeds))
humidity = np.zeros(len(seeds))
location = np.zeros(len(seeds))

humidity_to_location = pd.read_csv(r'C:\Users\Gabriel Marinho\OneDrive\Área de Trabalho\fun\AoC\humidity-to-location.csv', sep = ';')
temperature_to_humidity = pd.read_csv(r'C:\Users\Gabriel Marinho\OneDrive\Área de Trabalho\fun\AoC\temperature-to-humidity.csv', sep = ';')
light_to_temperature = pd.read_csv(r'C:\Users\Gabriel Marinho\OneDrive\Área de Trabalho\fun\AoC\light-to-temperature.csv', sep = ';')
water_to_light = pd.read_csv(r'C:\Users\Gabriel Marinho\OneDrive\Área de Trabalho\fun\AoC\water-to-light.csv', sep = ';')
fertilizer_to_water = pd.read_csv(r'C:\Users\Gabriel Marinho\OneDrive\Área de Trabalho\fun\AoC\fertilizer-to-water.csv', sep = ';')
soil_to_fertilizer = pd.read_csv(r'C:\Users\Gabriel Marinho\OneDrive\Área de Trabalho\fun\AoC\soil-to-fertilizer.csv', sep = ';')
seed_to_soil = pd.read_csv(r'C:\Users\Gabriel Marinho\OneDrive\Área de Trabalho\fun\AoC\seed-to-soil.csv', sep = ';')


# seed-to-soil
for s in range(0, len(seeds)):
     for i in range(0, len(seed_to_soil['z'])):
        if seeds[s] >= seed_to_soil['x'][i] and seeds[s] <= (seed_to_soil['x'][i] + seed_to_soil['y'][i]):
            seed_index = seeds[s] - seed_to_soil['x'][i]
            soil[s] = seed_to_soil['z'][i] + seed_index
        else:
            continue

if 0 in soil:   
    idx = np.where(soil == 0)
    soil[idx] = seeds[idx]
            
# soil-to-fertilizer
for s in range(0, len(seeds)):
     for i in range(0, len(soil_to_fertilizer['z'])):
        if soil[s] >= soil_to_fertilizer['x'][i] and soil[s] <= (soil_to_fertilizer['x'][i] + soil_to_fertilizer['y'][i]):
            soil_index = soil[s] - soil_to_fertilizer['x'][i]
            fertilizer[s] = soil_to_fertilizer['z'][i] + soil_index
        else:
            continue

if 0 in fertilizer:   
    idx = np.where(fertilizer == 0)
    fertilizer[idx] = soil[idx]

# fertilizer-to-water
for s in range(0, len(seeds)):
     for i in range(0, len(fertilizer_to_water['z'])):
        if fertilizer[s] >= fertilizer_to_water['x'][i] and fertilizer[s] <= (fertilizer_to_water['x'][i] + fertilizer_to_water['y'][i]):
            fertilizer_index = fertilizer[s] - fertilizer_to_water['x'][i]
            water[s] = fertilizer_to_water['z'][i] + fertilizer_index
        else:
            continue
    
if 0 in water:
    idx = np.where(water == 0)
    water[idx] = fertilizer[idx]

# water-to-light   
for s in range(0, len(seeds)):
     for i in range(0, len(water_to_light['z'])):
        if water[s] >= water_to_light['x'][i] and water[s] <= (water_to_light['x'][i] + water_to_light['y'][i]):
            water_index = water[s] - water_to_light['x'][i]
            light[s] = water_to_light['z'][i] + water_index
        else:
            continue

if 0 in light:
    idx = np.where(light == 0)
    light[idx] = water[idx]

# light-to-temperature
for s in range(0, len(seeds)):
     for i in range(0, len(light_to_temperature['z'])):
        if light[s] >= light_to_temperature['x'][i] and light[s] <= (light_to_temperature['x'][i] + light_to_temperature['y'][i]):
            light_index = light[s] - light_to_temperature['x'][i]
            temperature[s] = light_to_temperature['z'][i] + light_index
        else:
            continue

if 0 in temperature:
    idx = np.where(temperature == 0)
    temperature[idx] = light[idx]

# temperature-to-humidity
for s in range(0, len(seeds)):
     for i in range(0, len(temperature_to_humidity['z'])):
        if temperature[s] >= temperature_to_humidity['x'][i] and temperature[s] <= (temperature_to_humidity['x'][i] + temperature_to_humidity['y'][i]):
            temperature_index = temperature[s] - temperature_to_humidity['x'][i]
            humidity[s] = temperature_to_humidity['z'][i] + temperature_index
        else:
            continue

if 0 in humidity:
    idx = np.where(humidity == 0)
    humidity[idx] = temperature[idx]

# humidity-to-location
for s in range(0, len(seeds)):
     for i in range(0, len(humidity_to_location['z'])):
        if humidity[s] >= humidity_to_location['x'][i] and humidity[s] <= (humidity_to_location['x'][i] + humidity_to_location['y'][i]):
            humidity_index = humidity[s] - humidity_to_location['x'][i]
            location[s] = humidity_to_location['z'][i] + humidity_index
        else:
            continue

if 0 in location:
    idx = np.where(location == 0)
    location[idx] = humidity[idx]


print("Solution:", min(location))

