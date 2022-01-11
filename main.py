import eel
import json
from email.message import EmailMessage
import smtplib


eel.init("web2")


@eel.expose
def get_data(email, password):

    new_data = {
        email: {
            "password": password
        }
    }

    try:
        with open("data.json", mode="r") as datafile:
            data = json.load(datafile)

    except FileNotFoundError:
        with open("data.json", mode="w") as datafile:
            json.dump(new_data, datafile, indent=4)

    else:
        data.update(new_data)
        with open("data.json", mode="w") as datafile:
            json.dump(data, datafile, indent=4)

    finally:
        print("success")

    # now we should open the email app itself and close the log in menu


@eel.expose
def open_app():
    eel.init("web")
    eel.start("index.html", size=(1100, 580), block=False)

    @eel.expose
    def send(from_, to, subject, text):

        with open("data.json", mode="r") as datafile:
            data = json.load(datafile)
            e_password = data[f"{from_}"]["password"]

        email = EmailMessage()
        email["from"] = from_
        email["to"] = to
        email["subject"] = subject
        email.set_content(text)

        if "@gmail" in from_:
            data = smtplib.SMTP("smtp.gmail.com", port=587)
        elif "@outlook" in from_:
            data = smtplib.SMTP("outlook.office365.com", port=587)
        elif "@hotmail" in from_:
            data = smtplib.SMTP("smtp.live.com", port=587)
        elif "@yahoo" in from_:
            data = smtplib.SMTP("smtp.mail.yahoo.com", port=587)

        with data as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(from_, e_password)
            smtp.send_message(email)
            eel.notify()

@eel.expose
def send2(email):
    eel.send3(email)

eel.start("index2.html", size=(1100, 580))
