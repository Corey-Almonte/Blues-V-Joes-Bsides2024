import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import os

# Email configuration
smtp_server = "smtp.gmail.com"  # Gmail's SMTP server
smtp_port = 587  # TLS port
sender_email = "almontecorey98@gmail.com"

#export your password as an environment variable bro
password = os.getenv("EMAIL_PASSWORD")  # Retrieve password from environment variable

# Recipient details
recipient_email = "recipient@example.com"
subject = "Secure Email using TLS"
body = "This is a secure email sent using Python's smtplib with TLS encryption."

# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject

# Attach the body to the message
message.attach(MIMEText(body, "plain"))

# Create a secure SSL/TLS context
context = ssl.create_default_context()

try:
    # Connect to the SMTP server with TLS
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context=context)  # Start TLS encryption
        server.login(sender_email, password)  # Login to the email server
        server.sendmail(sender_email, recipient_email, message.as_string())  # Send the email
        print(f"Secure email sent successfully to {recipient_email}")

except Exception as e:
    print(f"Error: {e}")
