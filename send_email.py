import smtplib, ssl
import config

port = 587
smtp_server = config.mailServer
context = ssl.create_default_context()

def send_status_email(em_address, em_subject, em_body):
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.ehlo()
        server.login(config.username, config.pwd)
        subject =  em_subject
        body = em_body
        msg = f"subject: {subject}\n\n{body}"
        receiver_email = em_address
        server.sendmail(config.username, receiver_email, msg)

def send_mailBB():
    receiver_email = config.to_address
    subject = config.BB_prod["name"] + " is Now Available!"
    body = config.GS_prod["name"] + "now available at: \n" + config.BB_prod["url"]
    send_status_email(receiver_email, subject, body)
    
def send_mailGS():
    receiver_email = config.to_address
    subject = config.GS_prod["name"] + " is Now Available!"
    body = config.GS_prod["name"] + "now available at: \n" + config.GS_prod["url"]
    send_status_email(receiver_email, subject, body)

def send_mailUpdate(product_update):
    receiver_email = config.update_address
    subject =  "ASAP Hourly Summary"
    body = product_update
    send_status_email(receiver_email, subject, body)