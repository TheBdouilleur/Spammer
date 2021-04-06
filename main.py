'''Simple mail spammer
@author: TheBdouilleur
@license: MIT license
@date: 24/03/2020
'''
import smtplib
import time
from sampleData import *

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

useSampleData = bool(input('Use sample data?'))
if not useSampleData:
    sender = str(input('Who are you, miserable murderer?(enter email adress): '))
    password = str(input('What is your secret key?(enter password): '))
    receiver = str(input('Who will die tonight thanks to your kindness?(enter email adress): '))
    text = str(input('WHat type of knife shall be used on this fateful night by your fateful knight?(enter email text to send) :'))
    subject = str(input('What shall I say before the murder? (enter email subject): '))
    mails = str(input('How much stabs will he receive?(enter desired number of emails): '))

msg = MIMEMultipart() 
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject
html = '''
 <!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title></title>
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>

<body class="stackedit">
  <div class="stackedit__html">
<p>{}<p>
</div>
</body>

</html>
'''.format(text)

body = MIMEText(html, 'html') 
msg.attach(body)

startTime = time.time()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)

for i in range(1, int(mails)+1): 
    # time.sleep(0.1) #If script causes computer crash, uncomment this line
    refuses = 0
    disconnections = 0
    try:
        try:
            server.sendmail(sender, receiver, msg.as_string()) 
            print(f'sent {i}') 
        
        except smtplib.SMTPSenderRefused:
            refuses += 1
            print(f'Sender refused({refused}).')
            print('Waiting for ban timeout (60s)...')
            time.sleep(60)
            print('60s elapsed')
            print('Retrying...')
    
        except smtplib.SMTPServerDisconnected:
            disconnections += 1
            print(f'Server aborted({disconnected}).')
            print('Reconnecting...')
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, password)

       
    except KeyboardInterrupt: # If computer on the edge of crashing, or other abort reason, press Ctrl C 
        server.quit()
        print('aborted')
        break

print(f'Sent {i} messages in {time.time()-startTime} seconds to {receiver} with {sender}.\n {disconnections} server disconnections and {refuses} sender refuses.')