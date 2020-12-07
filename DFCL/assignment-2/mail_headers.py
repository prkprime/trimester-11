'''
Author : Pratik Gorade
Email : pratikgorade0@gmail.com
'''

import imaplib
import email
from email.parser import HeaderParser
from decouple import config

host = config('HOST')
email_id = config('EMAIL')
password = config('PASSWORD')

parser = HeaderParser()

imap = imaplib.IMAP4_SSL(host=host)
imap.login(user=email_id, password=password)

status, total_emails = imap.select('INBOX')

res, mail = imap.fetch(str(int(total_emails[0])), "(RFC822)")
for response in mail:
    if isinstance(response, tuple):
        response = email.message_from_bytes(response[1])
        headers = parser.parsestr(response.as_string())
        for header, val in headers.items():
            print(f'{header} : {val}')