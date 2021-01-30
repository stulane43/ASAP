import smtplib, ssl
import config

# Mail Server
port = 587
server = smtplib.SMTP(config.mailServer, port)
context = ssl.create_default_context()
server.ehlo()
server.starttls(context=context)
server.ehlo
server.login(config.username, config.pwd)

def send_mailBB():
    subject = config.BB_prod["name"] + " is Now Available!"
    body = "Your Item is now available at: \n" + config.BB_prod["url"]
    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
        config.username,
        config.to_address,
        msg
    )
    
def send_mailGS():    
    subject = config.GS_prod["name"] + " is Now Available!"
    body = "Your Items is now available at: \n" + config.GS_prod["url"]
    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
        config.username,
        config.to_address,
        msg
    )

def send_mailUpdate():    
    subject =  "ASAP Update"
    body = "Your Item is still Out of Stock"
    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
        config.username,
        config.update_address,
        msg
    )