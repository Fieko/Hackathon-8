from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'codefriendlyvsu@gmail.com'
email_password = 'ydjhkctorziqkfnz'
email_reciever = 'darienwalker121@outlook.com'
student1 = "Nicholas"
 
subject = 'STUDENT ACADEMIC WARNING'
body = """
NOTICE: Your student """ + student1 + """ is currently in Academic Warning status. Please email your student and schedule an appointment.


"""


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
