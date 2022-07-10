import smtplib
from decouple import config


SENDER_EMAIL = config('USER_EMAIL')
PASSWORD = config('EMAIL_PASSWORD')
receiver_email = 'dev.freddoe@gmail.com'

smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# try:
#     smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# except:
#     print("Connection  failed")
# else:
#     with smtp_server:
#         smtp_server.login(SENDER_EMAIL, PASSWORD)

#         subject = "Testing the Email Code"
#         body = """
#         Let us test this email.
#         This is a test email to try emailing with Python.net
#         """

#         msg = f"Subject: {subject}\n\n{body}"
#         try:
#             smtp_server.sendmail(SENDER_EMAIL, receiver_email, msg)
#         except:
#             print("Error sending mail")
#         else:
#             print("Mail successfully sent!")