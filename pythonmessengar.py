##Below 2 script may use to send e-mails.

import smtplib
server = smtplib.SMTP_SSL('smtp.yandex.com.tr', 465)
server.login("mustafa.akgull@yandex.com", "pinkamoeba_4U")
msg = "This script written by akgul!" # The /n separates the message from the headers
server.sendmail("mustafa.akgull@yandex.com", "mustafa.akgull@yandex.com", msg)



import smtplib
def send_emails(title,msg):
    server = smtplib.SMTP_SSL('smtp.yandex.com.tr', 465)
    ##server = smtplib.SMTP('smtp.yandex.com.tr:465')
    server.ehlo()
    ##server.starttls()
    server.login("mustafa.akgull@yandex.com", "pinkamoeba_4U")
    message = 'Subject: {}\n\n{}'.format(title,msg)
    server.sendmail("mustafa.akgull@yandex.com", "mustafa.akgull@yandex.com",message)
    server.quit()
    print("E-mails successfully sent!")

send_emails('Test Mail From Akgul', 'This e-mail has been sent by akgul!')
