##################### Extra Hard Starting Project ######################
from calendar import month
import datetime as dt
import smtplib
import pandas as pd
import random
import os

my_email = "contact.harshvardhansingh@gmail.com"
password = "mrgreen9416"
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = now.day
Month = now.month
birthday = pd.read_csv("birthdays.csv")
for (index,row) in birthday.iterrows():
    if today == row["day"] and Month == row["month"]:
        file = random.choice(os.listdir("letter_templates/"))
        with open(f"letter_templates/{file}", "r") as temp:
            data = temp.read()
            new_data = data.replace("[NAME]", row['name'])
    
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user= my_email, password= password)
            connection.sendmail(from_addr= my_email, to_addrs=row["email"] , msg= f"Subject:Happy Birthday\n\n{new_data}")



    

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




