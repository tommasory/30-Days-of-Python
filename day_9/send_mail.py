import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# environment variables
"""
EXAMPLES
0. python -i day_9/send_mail.py
1. send_mail(to_emails=['develop.tomas@gmail.com'],credentials={"username":"ISSUER_MAIL","password":"ISSUER_PASSWORD"})
2. send_mail(to_emails=['develop.tomas@gmail.com'], html='<h1>This is working</h1>',credentials={"username":"ISSUER_MAIL","password":"ISSUER_PASSWORD"})
"""
def send_mail(text='Email Body', subject='Hello World', from_email='Hungry Py <develop.tomas@gmail.com>', to_emails=None, html=None, credentials={}):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)
        
    msg_str = msg.as_string()
    # login to my smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(credentials['username'], credentials['password'])
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()
