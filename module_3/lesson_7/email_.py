import smtplib
import threading
import time
from email.message import EmailMessage


email_address = "absaitovdev@gmail.com"
email_password = "lrtigfroqxwqulrk"


mail_list = [

"saidakbaruraimov7@gmail.com",
"mohirmirahmadov@gmail.com",
"zoirbekergashev4567@gmail.com",
"khayrullo.devs@gmail.com",
"imonqulovf1234@gmail.com",
"samidilloravshanov13@gmail.com",
"shahrizodaxakimova12@gmail.com",
"shohjahonobruyev3@gmail.com",
"diyorbekdilmurodov1@gmail.com",
"suratovdoniyor@gmail.com",
"dilshodbekakhmatov@gmail.com",
"nurillayevezozbek@gmail.com",
# "saidakbaruraimov7@gmail.com",
# "mohirmirahmadov@gmail.com",
# "zoirbekergashev4567@gmail.com",
# "azamovshahboz06082001@gmail.com",
# "boburkhonov99@mail.ru",
# "doniyorbek068@gmail.com",
# "ahmatovdilshodbek@gmail.com",
# "isomiddinwtu@gmail.com",
# "kodirovadilfuza9706@gmail.com",
# "turgunovjamshid32@gmail.com",
# "nabiyevadilnavoz736@gmail.com"
             ]

def send_mail(mail):
        msg = EmailMessage()
        msg['Subject'] = "Email subject"
        msg['From'] = email_address
        msg['To'] = mail
        msg.set_content("This is eamil message")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

            smtp.login(email_address, email_password)
            smtp.send_message(msg)
            print("send mail !")

l = []
start = time.time()
for i in mail_list:
    t = threading.Thread(target=send_mail , args=(i,))
    t.start()
    l.append(t)

for i in l:
    i.join()

print(time.time() - start)

