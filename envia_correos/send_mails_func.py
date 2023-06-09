import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender, recipient, subject, message, password):
    """Sends an email using the SMPT server"""
    try:
        # Create a secure connection with SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to the sender´s email account
        server.login(sender, password)

        # Create a multipart message
        email_message = MIMEMultipart()
        email_message['From'] = sender
        email_message['To'] = recipient
        email_message['Subject'] = subject

        # Attach the message to the email
        email_message.attach(MIMEText(message, 'plain'))

        # Send the email
        server.send_message(email_message)

        print('Email sent successfully!')
    except Exception as e:
        print('An error occurred while sending the email: ', str(e))
    finally:
        server.quit()


