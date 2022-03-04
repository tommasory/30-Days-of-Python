import sys
import requests
from datetime import datetime

from formatting import format_msg
from send_mail import send_mail

def send(name, website=None, to_email=None, verbose=False,credentials={}):
    assert to_email != None
    if website != None:
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)
    if verbose:
        print(name, website, to_email)
    # send the message
    try:
        send_mail(text=msg, to_emails=[to_email], html=None,credentials=credentials)
        sent = True
    except:
        sent = False
    return sent

"""
EXAMPLES

1. python day_9/send.py NAME RECIPIENT_MAIL ISSUER_MAIL ISSUER_PASSWORD
"""
if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    credentials = {}

    if len(sys.argv) > 1:
        name = sys.argv[1]

    email_receiver = None
    if len(sys.argv) > 2:
        email_receiver = sys.argv[2]

    if len(sys.argv) > 3:
        credentials['username'] = sys.argv[3]
        credentials['password'] = sys.argv[4]

    response = send(name, to_email=email_receiver, verbose=True, credentials=credentials)
    print(response)