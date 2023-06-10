from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_registration_email(subject: str, message: str, from_email: str,
                            recipient_list: list) -> None:
    """Send registration notification by email."""
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False,
    )
