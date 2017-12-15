"""
Web analyzer that searches for content in raw pages and notifies accordingly.
"""

import smtplib
import urllib.request
from collections import namedtuple
from email.mime.text import MIMEText

SMTPDetails = namedtuple("SMTP", "address port tls username password sender recipients")

def check(url, tokens, matchall=False):
    """
    Checks the given URL's raw HTML content for the presence of any of the given tokens.
    Set matchall to True to match all the tokens at once instead.
    """

    urlopener = urllib.request.FancyURLopener({})
    content = urlopener.open(url).read()
    for token in tokens:
        if matchall:
            if str(content).find(token) == -1:
                return False
        else:
            if str(content).find(token) != -1:
                return True
    return True if matchall else False


def notify(smtpdetails, subject, message):
    """
    Sends an email via the given SMTP server.
    smtpdetails corresponds to the module's internal named tuple SMTPDetails.
    """

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = smtpdetails.sender
    msg['To'] = ', '.join(smtpdetails.recipients)

    try:
        server = smtplib.SMTP(smtpdetails.address, smtpdetails.port)
        if smtpdetails.tls:
            server.starttls()
        if smtpdetails.username and smtpdetails.password:
            server.login(smtpdetails.username, smtpdetails.password)
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPException as e:
        print("Unable to send mail: {}".format(e))
