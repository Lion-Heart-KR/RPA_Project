import smtplib
from account import *
from email.message import EmailMessage
from random import *

nicknames = ["유재석", "이광수", "조세호", "김종국", "송지효", "전소민"]

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS_GOOG, EMAIL_PASSWORD_GOOG)
    
    for nickname in nicknames:
        msg = EmailMessage()
        msg["Subject"] = "파이썬 특강 신청합니다."
        msg["From"] = EMAIL_ADDRESS_GOOG
        msg["To"] = EMAIL_ADDRESS_NAVER

        # content = nickname + "/" + str(randint(1000, 9999))
        content = "/".join([nickname, str(randint(1000, 9999))])
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname + "님으로부터 메일이 도착했습니다.")