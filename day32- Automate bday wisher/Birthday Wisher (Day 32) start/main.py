import smtplib

my_email = "contact.harshvardhansingh@gmail.com"
password = "mrgreen9416"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

#     #now lets make our connection secure
#     connection.starttls()   #transport layer server

#     #now lets login
#     connection.login(user= my_email, password= password)
    
#     #send mail
#     connection.sendmail(from_addr= my_email, to_addrs="prashant.pk45@gmail.com", msg= "Subject:Maar Khaega\n\njaldi se aao bangalore, ni to maar khaega")

    #connection.close()
    # if i didnt use with keyword, then i have to close the connection.


import datetime as dt
import random

today = dt.datetime.now()
year = today.year
month = today.month
day_of_the_week = today.weekday()
date_of_birth = dt.datetime(year=1993, month=3, day=16)

if day_of_the_week == 0:
    with open("quotes.txt") as quotes:
        lines = quotes.readlines()
        quote = random.choice(lines)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user= my_email, password= password)
        connection.sendmail(from_addr= my_email, to_addrs="contact.meenakshisingh@gmail.com", msg= f"Subject:Motivation\n\n{quote}")



