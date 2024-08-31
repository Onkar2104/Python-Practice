from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def send_email_to_client():
    subject = "This email is from django"
    message = "This is a tast email from django"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["onkarijare2104@gmail.com"]

    send_mail(subject, message, from_email, recipient_list)

def send_email_with_attachment(subject, message, recipient_list, file_path):
    mail = EmailMessage(subject=subject, body = message, from_email = settings.EMAIL_HOST_USER, to = recipient_list)

    mail.attach_file(file_path)
    mail.send()