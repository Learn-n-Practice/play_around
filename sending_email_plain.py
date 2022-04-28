import smtplib
from decouple import config


SENDER_EMAIL = config('USER_EMAIL')
PASSWORD = config('EMAIL_PASSWORD')
receiver_email = 'dev.freddoe@gmail.com'

try:
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
except:
    print("Connection  failed")
else:
    with smtp_server:
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()

        smtp_server.login(SENDER_EMAIL, PASSWORD)

        subject = "Testing the Email Code"
        body = """
        Let us test this email.
        This is a test email to try emailing with Python.net
        """
        msg = f"Subject: {subject}\n\n{body}"
        try:
            smtp_server.sendmail(SENDER_EMAIL, receiver_email, msg)
        except:
            print("Error sending mail")
        else:
            print("Mail successfully sent!")