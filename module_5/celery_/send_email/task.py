import smtplib
from email.message import EmailMessage
import celery

app = celery.Celery("main" , broker="redis://localhost:6379/0")


@app.task()
def send_email(email):
    email_address = "absaitovdev@gmail.com"
    email_password = "dglhclifstiydtym"
    msg = EmailMessage()
    msg['Subject'] = "Email subject"
    msg['From'] = email_address
    msg['To'] = email
    msg.set_content("This is eamil message")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        print("send mail !")