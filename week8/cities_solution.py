from cities import CITIES

# Split the CITIES string into a list of its rows
CITIES = CITIES.split('\n')

# Define empty dicts
province_to_city = {}
city_to_province = {}

# Loop over each row, split it into province, city and area
for city in CITIES:
    province, city, area = city.split(',')
    area = float(area)

    # Check if the key does not exist. If it doesn't exist, construct a new list at that key
    if not province in province_to_city:
        province_to_city[province] = [(city, area)]
    else: # Key exists, append to the list
        province_to_city[province].append((city, area))

    city_to_province[city] = province

# Find out what province has the most and least number of cities
max_num_cities = 0
min_num_cities = float('inf')

for province in province_to_city:
    num_cities = len(province_to_city[province])

    if num_cities > max_num_cities:
        max_num_cities = num_cities
        province_max_cities = province
    elif num_cities == max_num_cities: # Tie-breaker
        province_max_cities = min(province, province_max_cities)

    if num_cities < min_num_cities:
        min_num_cities = num_cities
        province_min_cities = province
    elif num_cities == min_num_cities: # Tie-breaker
        province_min_cities = max(province, province_min_cities)

# Note: several provinces only have 1 city
print('Province with the max number of cities is', province_max_cities, 'with', max_num_cities, 'cities.')
print('Province with the min number of cities is', province_min_cities, 'with', min_num_cities, 'cities.')

# Find out which province has the greatest municipal land area
max_area = 0.

for province in province_to_city:
    area = 0.

    for city in province_to_city[province]:
        area += city[1] # Second element of the tuple contains land area

    if area > max_area:
        max_area = area
        province_max_area = province

print('Province with the max municipal land area is', province_max_area, 'with a municipal area of', max_area, 'km^2.')

# Find out what province Merrit is in
print('Merritt is in ', city_to_province['Merritt'], '.', sep='')