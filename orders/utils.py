from django.core.mail import send_mail


def send_email(user):
    send_mail(
        'order success',
        'your order is success ' + str(user),
        'from@example.com',
        ['to@example.com'],
    )
