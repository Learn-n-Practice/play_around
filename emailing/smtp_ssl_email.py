import smtplib
from decouple import config


SENDER_EMAIL = config("SENDER_EMAIL")
PASSWORD = config("EMAIL_PASSWORD")
RECEIVER_EMAIL = config("RECEIVER_EMAIL")


try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
except:
    print("Connection  failed")
else:
    with smtp_server:
        smtp_server.login(SENDER_EMAIL, PASSWORD)

        subject = "Testing the Email Code"
        body = """
        Let us test this email.
        This is a test email to try emailing with Python.net
        """

        msg = f"Subject: {subject}\n\n{body}"
        try:
            smtp_server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg)
        except:
            print("Error sending mail")
        else:
            print("Mail successfully sent!")