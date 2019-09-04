import smtplib
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_mail(subiect, message_body, file):
    attach_file_name = file
    receiver_address = config.RECEIVER
    sender = config.SENDER
    mail_username = config.MAIL_USERNAME
    mail_password = config.MAIL_PASSWORD
    mail_serwer = config.MAIL_SERVER
    mail_port = config.MAIL_PORT

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver_address
    msg['Subject'] = subiect

    msg.attach(MIMEText(message_body))
    attach_file = open(file, 'rb')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
    msg.attach(payload)

    session = smtplib.SMTP(mail_serwer, mail_port)
    session.starttls()
    session.login(mail_username, mail_password)
    text = msg.as_string()
    session.sendmail(sender, receiver_address, text)
    session.quit()
