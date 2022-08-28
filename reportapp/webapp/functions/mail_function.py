from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import threading

def send_mail(username,mail,verificationcode):
    subject = 'Verificar correo electrónico'
    template = get_template('welcome_mail.html')

    content = template.render({
        'username': username,
        'verificationcode': verificationcode
    })

    message = EmailMultiAlternatives(subject, #Titulo
                                    '',
                                    settings.EMAIL_HOST_USER, #Remitente
                                    [mail]) #Destinatario

    message.attach_alternative(content, 'text/html')
    message.send()

def send_pdf(username,mail,urldoc):
    subject = 'Confirmación de cita'
    template = get_template('pdf_mail.html')

    content = template.render({
        'username': username,
        'urldoc': urldoc
    })

    message = EmailMultiAlternatives(subject, #Titulo
                                    '',
                                    settings.EMAIL_HOST_USER, #Remitente
                                    [mail]) #Destinatario

    message.attach_alternative(content, 'text/html')
    message.send()