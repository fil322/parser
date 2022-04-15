import smtplib
import os

import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart


def send_email(addr_from, passwor, addr_to, files):
    msg_subj = 'Password'
    msg_text = 'Password'
    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = msg_subj

    body = msg_text
    msg.attach(MIMEText(body, ' plain'))

    process_attachement(body, 'plain')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(addr_from, passwor)
    server.send_message(msg)
    server.quit()


def process_attachement(msg, files):
    for f in files:
        if os.path.isfile(f):
            attach_file(msg, f)
        elif os.path.exists(f):
            dir = os.listdir(f)
            for file in dir:
                attach_file(msg, f + "/" + file)


def attach_file(msg, filepath):
    filename = os.path.basename(filepath)
    ctype, encoding = mimetypes.guess_type(filepath)
    if ctype is None or encoding is None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    if maintype == 'text':
        with open(filepath) as fp:
            file = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
    elif maintype == 'image':
        with open(filepath, 'rb') as fp:
            file = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
    elif maintype == 'audio':
        with open(filepath) as fp:
            file = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
    else:
        with open(filepath, 'rb') as fp:
            file = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
            encoding.encode_base64(file)
    file.add_header('Content-Dispotion', 'attachment', filename=filename)
    msg.attach(file)

_from = 'gmail'
_password = 1111
_to = 'gmail'
files = ["pass.txt"]

send_email(_from, _password, _to, files)

server = smtplib.SMTP_SSL('smtp.mail.ru', 25)
server.login(addr_from, passwor)
server.send_message(msg)
server.quit()