import smtplib
import config

# Mail Server
server = smtplib.SMTP(config.mailServer, 587)
server.ehlo()
server.starttls()
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
        config.username,
        msg
    )