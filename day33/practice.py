from time import time
from urllib import response
import requests
from datetime import datetime
import smtplib

MY_LAT = 12.971599
MY_LNG = 77.594566

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  #- raises exception

data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (longitude, latitude)



Parameters = {
    "lat": MY_LAT ,
    "lng": MY_LNG ,
    "formatted": 0
}

my_email = "contact.harshvardhansingh@gmail.com"
password = "mrgreen9416"


response_1 = requests.get(url= "https://api.sunrise-sunset.org/json", params=Parameters)
response_1.raise_for_status()
new_data = response_1.json()
print(new_data)
sunrise = float(new_data["results"]["sunrise"].split("T")[1].split(":")[0]) + 5
sunset = float(new_data["results"]["sunset"].split("T")[1].split(":")[0]) + 5

time_now = datetime.now()
cur_hour = time_now.hour
def look_up():
    if abs(MY_LAT - latitude) <= 5 and abs(MY_LNG - longitude) <= 5:
        if sunrise > cur_hour or cur_hour > sunset:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user= my_email, password= password)
                connection.sendmail(from_addr= my_email, to_addrs="prashant.pk45@gmail.com" , msg= f"Subject:ISS\n\nLookup")

        


