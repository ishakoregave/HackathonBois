
import pandas as pd
import math

# user information
name = input("Enter your name : ")
age = input("Enter your age : ")
sex = input("Enter your sex (Male/Female): ")
number = input("Enter your contact number including your +1:")

# symptoms

score = 0

print("Do you have fever over 100 degrees Fahrenheit? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score = s+5

print("Do you have cough? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score = s+5

print("Do you have shortness of breath or difficulty in breathing? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score += s

print("Do you have fatigue or chills? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score += s

print("Do you have muscle aches or pain? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score += s

print("Do you have Headache? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score += s

print("Do you have a new loss of taste or smell? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score += s

print("Do you have sore throat? 1 means yes, 0 means no ")
s = int(input("Enter answer : "))
score += s

print("were you in contact with infected person (1 mean yes, 0 mean no)")
contact = int(input("enter answer : "))

# condition and next steps based on score
next_steps = 0
if score > 5 :
    print ("must do a covid-19 test.You may be infected with covid-19. We will be accessing your devices information to help you find the nearest open covid testing center")
    next_steps = 1
elif score < 3:
    print("you must isolate yourself for 5 days, if no more symptoms then you are not infected ")
else :
    if contact == 1 :
        print("You must Isolate for 14 days and do a covid-19 test.We will be accessing your devices information to help you find the nearest open covid testing center")
        next_steps = 1
    else :
        print("Isolate for 7 days if no more symptoms then you are not infected")


if next_steps == 1:


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




