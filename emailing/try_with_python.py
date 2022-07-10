# Import smtplib for the actual sending function
import smtplib
from decouple import config

# Import the email modules we'll need
from email.message import EmailMessage

SENDER_EMAIL = config("SENDER_EMAIL")
PASSWORD = config("EMAIL_PASSWORD")
RECEIVER_EMAIL = config("RECEIVER_EMAIL")

text = """
This is a message from the development phase
"""

msg = EmailMessage()
msg.set_content(text)

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = "This is the Subject"
msg['From'] = SENDER_EMAIL
msg['To'] = RECEIVER_EMAIL

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()