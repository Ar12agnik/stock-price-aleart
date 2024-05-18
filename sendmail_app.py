import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_mail_msg(message):
    sender_email = "help.devvendors@gmail.com"
    receiver_email = "ar12agnik@gmail.com"
    subject = "Your Stock Alert"
    body = f"{message}"

    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Connect to Gmail SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "help.devvendors@gmail.com"
    smtp_password = 'kctg tgwo cuii ggqg'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Start TLS encryption
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully.")
