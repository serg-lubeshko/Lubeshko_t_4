import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from dotenv import load_dotenv

load_dotenv()


def send_mail(users_mail: list, email_template: str, context: dict, subject: str):
    port = os.environ.get('PORT')
    smtp_server = os.environ.get('SMTP_SERVER')
    sender_email = os.environ.get('SENDER_EMAIL')
    password = os.environ.get('PASSWORD')
    # subject = "Секретный пароль"
    email_template_name = email_template
    # message = """This Message is send from python script"""
    # receiver_email = []

    # cont = {'email': users_mail,
    #         'domain': '127.0.0.1:8000',  # Доменное имя сайта
    #         # 'site_name': 'ITTAS', #Название своего сайта
    #         # 'uid': urlsafe_base64_encode(force_bytes(user1.pk)),  # Шифруем идентификатор
    #         # 'token': default_token_generator.make_token(user1),  # Генерируем токен
    #         'protocol': 'http',
    #         # 'user': user1
    #         }

    msg_html = render_to_string(email_template_name, context)
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['To'] = ','.join(users_mail)
    msg['From'] = sender_email
    html = MIMEText(msg_html, 'html')
    msg.attach(html)

    try:
        mail = smtplib.SMTP(smtp_server, port)
        context = ssl.create_default_context()
        mail.ehlo()
        mail.starttls(context=context)
        mail.ehlo()
        mail.login(sender_email, password)
        mail.sendmail(sender_email, users_mail, msg.as_string())
        # mail.sendmail(sender_email,receiver_email, message)
        mail.quit()
    except BadHeaderError:
        return HttpResponse('Обнаружен недопустимый заголовок!')
    # return redirect('password_reset_done')
