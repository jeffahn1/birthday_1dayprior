from datetime import datetime, date, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, False))

environ.Env.read_env(BASE_DIR / '.env')

APP_PASSWORD = env("APP_PASSWORD")


def send_reminder_email(friend, birthday):
    EMAIL = "ahnjnyc@gmail.com"
    PASSWORD = APP_PASSWORD
    EMAIL_TO = "ahnjnyc@gmail.com"
    # send email reminder to self

    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = EMAIL_TO
    msg["Subject"] = "Birthday Reminder"

    body = f"This is a reminder that it's {friend}'s birthday tomorrow!"
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL, EMAIL_TO, text)
    server.quit()


# create dictionary of key(name):value(birthday) pairings
def birthday():
    my_friends_dict = {
        "Benji": "06/20/1997",
        "Stefan": "04/11/1997",
        "Nes": "11/14/1996",
        "Jad": "05/26/2000",
        "Eric": "09/21/2001",
        "Jared": "04/30/1999",
        "Zacchai": "07/24/2002",
        "Test": "11/12/2023"
    }
    today = date.today()
    tomorrow = today + timedelta(days=1)
    for friend, birthday in my_friends_dict.items():
        # format birthday string to be datetime object
        birthday = datetime.strptime(birthday, "%m/%d/%Y").date()
        print(tomorrow.strftime("%m/%d"), birthday.strftime("%m/%d"))

        if birthday == tomorrow:
            print("Sending myself reminder email")
            # send reminder email to myself
            send_reminder_email(friend, birthday)


birthday()
