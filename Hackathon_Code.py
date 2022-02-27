
import pandas as pd
import math

centre_locations = pd.read_csv("centre_locations.csv")
#print(centre_locations)

latitudes = []
longitudes = []
for i in range(len(centre_locations.index)):
    str1 = centre_locations["JSON"][i]

    import http.client

    conn = http.client.HTTPSConnection("google-maps-geocoding.p.rapidapi.com")
    headers = {
        'x-rapidapi-host': "google-maps-geocoding.p.rapidapi.com",
        'x-rapidapi-key': "64a2c6e7e1mshb84cb6a6df3feedp196c9fjsnb64d7956ace6"
    }
    conn.request("GET", str1, headers=headers)
    res = conn.getresponse()
    data = res.read()
    str2 = (data.decode("utf-8"))

    latitudes.append(float((data.decode("utf-8"))[((data.decode("utf-8")).find("lat") + 7):((data.decode("utf-8")).find("lat") + 16)]))
    longitudes.append(float((data.decode("utf-8"))[((data.decode("utf-8")).find("lng") + 7):((data.decode("utf-8")).find("lng") + 18)]))

centre_locations['latitudes'] = latitudes
centre_locations['longitudes'] = longitudes

import phonenumbers
from phonenumbers import geocoder
number = input("Pease number: ")
key = "06a067a51a8b4290b8678be0c5b1ab4f"

n = phonenumbers.parse(number)
l = geocoder.description_for_number(n, "en")
print(l)

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(l)
result = geocoder.geocode(query)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)


min_dist = []

for i in range(len(centre_locations.index)):
    x1 = centre_locations["latitudes"][i]
    y1 = centre_locations["longitudes"][i]
    minboi = math.sqrt((lat-x1)*(lat-x1) + (lng-y1)*(lng-y1))
    min_dist.append(minboi)

centre_locations['minimum distance'] = min_dist
print(centre_locations)




