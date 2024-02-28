places = {("19.07'53.2", "72.54'51.0"):"Mumbai", \
          ("28.33'34.1", "77.06'16.6"):"Delhi"}

print(places)
print()

lat = []
long = []
plc = []
for i in places:
    lat.append(i[0])
    long.append(i[1])
    plc.append(places[i[0], i[1]])

print(lat)
print(long)
print(plc)
print()

# i[0] is the latitude.
# i[1] is the longitude.
# places[i[0], i[1]] gets the value associated with the current key, which is the place name (e.g., "Mumbai" or "Delhi").


places = {
    ("19.07'53.2", "72.54'51.0"): "Mumbai",
    ("28.33'34.1", "77.06'16.6"): "Delhi",
    ("34.05'12.5", "118.24'18.0"): "Los Angeles"
}

# Traversing the dictionary and creating lists
latitudes = []
longitudes = []
locations = []

for coordinates, location in places.items():
    latitudes.append(coordinates[0])
    longitudes.append(coordinates[1])
    locations.append(location)

print("Latitudes:", latitudes)
print("Longitudes:", longitudes)
print("Locations:", locations)
