'''The file email.txt contains a raw email. Write a program that uses regular expressions to fetch and print:

sender email address
recipient email address
email subject
email body
For each of the above commands, define a separate function (see below) that returns the value read from the email. Place the functions in a separate module called emails.

email_sender()
email_recipient()
email_subject()
email_body()'''


import re

def email_sender(filename):
    pattern = '([a-z]{3}\.[a-z]{8}@[a-z]{7}\.[a-z]{3})'
    with open(filename) as f:
        content = f.read()

    info = re.findall(pattern, content)
    
    emails= list(set(info))
    return emails[0]

def email_recipient(filename):
    pattern = '([a-z]{4}\.[a-z]{5}@[a-z]{7}\.[a-z]{3})'
    with open(filename) as f:
        content = f.read()

    info = re.findall(pattern, content)
    
    emails= list(set(info))
    return emails[0]

def email_subject(filename):
    pattern = '([A-z][a-z]{5}) ([a-z]{7})'
    with open(filename) as f:
        content = f.read()

    info = re.findall(pattern, content)

    return info

def email_body(filename):
    pattern = '(^I[A-Za-z\s\S]+\.$)'
    with open(filename) as f:
        content = f.read()

    info = re.findall(pattern, content)

    return info

print(email_body('email.txt'))