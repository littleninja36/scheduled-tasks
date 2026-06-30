# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

PLACEHOLDER = "[NAME]"

# 1. Update the birthdays.csv
#my version
birthdays = pd.read_csv("birthdays.csv").to_dict("records")
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
# course version
today_tuple = (now.month,now.day)

#course version
for line in birthdays:
    month = int(line["month"])
    day = int(line["day"])
    if (month,day) == today_tuple:

# # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{randint(1, 3)}.txt") as file:
            letter = file.read()
            birthday_letter = letter.replace(PLACEHOLDER, line["name"])
            recipient_email = line["email"]
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com',587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=recipient_email,
                                msg=f"Subject:Happy Birthday!\n\n{birthday_letter}")
