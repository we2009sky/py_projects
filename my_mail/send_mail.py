# encoding=utf8

import smtplib
from email.mime.text import MIMEText

HOST = 'smtp.qq.com'
SENDER = '1058674551@qq.com'
PASSWORD = 'LWZ09220922'
RECEIVER = SENDER


def send_email():
    message = 'This mail send by python'
    msg = MIMEText(message)
    msg['Subject'] = 'hello world'
    msg['From'] = SENDER
    msg['To'] = SENDER

    smtp_server = smtplib.SMTP()
    try:
        smtp_server.connect(HOST)
        smtp_server.login(SENDER,PASSWORD)
        smtp_server.sendmail(SENDER, SENDER, msg.as_string())
    except Exception as e:
        print(e)
    finally:
        smtp_server.quit()


if __name__ == '__main__':
    send_email()