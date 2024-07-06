from email.message import EmailMessage  # Importing from Python library.
from keys import password   # Importing variable from file in same directory.
import ssl  # Importing secure TLS connection.
import smtplib  # Importing module from Python library to send email.

# Assigning variables.
email_sender = '***'    # User-sender email.
email_password = password   # Imported variable containing passsword.
email_receiver = '***'  # User who receives the email.
subject = "Email sender program using Python"
body = """
Salutations and Congratulations on achieving your "First case of an actual
email sender program I made using Python" project! This marks another step
taken forward towards your programming journey!
"""

# Using class properties respectively.
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Creating a secure connection to send email.
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("Email sent successfully!")
