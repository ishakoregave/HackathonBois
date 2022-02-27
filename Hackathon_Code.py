
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

if score > 7:
    print("You are being directed to hospitals near you, please make sure you get admitted immediately")
elif 7>=score >=4 :
    print ("Must do a covid-19 test.You may be infected with covid-19. We will be accessing your devices information to help you find the nearest open covid testing center")
    next_steps = 1
elif 0< score =< 3:
    print("you must isolate yourself for 5 days, if no more symptoms then you are not infected. We will be accessing your devices information and providing you with information regarding resources such as masks are available. ")
else :
    if contact == 1 :
        print("You must Isolate for 14 days and do a covid-19 test.We will be accessing your devices information to help you find the nearest open covid testing center")
    else :
        print("Isolate for 7 days if no more symptoms then you are not infected")
        quit()



centre_locations = pd.read_csv("total_database1.csv")
#print(centre_locations)

import phonenumbers
from phonenumbers import geocoder

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
#print(centre_locations)




centre_locations.sort_values(by=['minimum distance'], inplace=True)

#get date, day and time of user and filter data accordingly
from datetime import datetime
from datetime import date


now = datetime.now()
today = date.today()
print("Today's date:", today)

current_time = now.strftime("%H%M")
print("Current Time =", current_time)

weekday = datetime.weekday(today)
print("Current Day=", weekday)
# int value range: 0-6, monday-sunday
if weekday <5:
    day_range = "M-F"
elif weekday >= 5:
    day_range = "M-S"
print(day_range)

centre_locations[(centre_locations['Opens at'] <= current_time) & ( current_time<= centre_location['Closes at'])&(centre_location['Days open']==day_range)]


admit_locations = centre_locations.loc[centre_locations['Doctor Consultation AND ADMIT'] == 'Y']
vaccine_locations = centre_locations.loc[centre_locations['Vaccine Available'] == 'Y']
mask_locations = centre_locations.loc[centre_locations['Masks'] == 'Y']
testing_locations = centre_locations.loc[centre_locations['testing'] == 'Y']
home_locations = centre_locations.loc[centre_locations['home testing'] == 'Y']

print(testing_locations)
