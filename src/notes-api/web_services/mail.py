from django.core.mail import send_mail
from django.conf import settings

def _send_message(subject, message, recipient):
    """Sends message to an email. """
    return send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient],
        fail_silently=False,
    )


def send_signup_message(email: str, username: str):
    """Sends welcome signup message to an email."""
    return _send_message(
        "Signup on Notes", 
        f"Hello, {username}! Welcome to the Notes!", 
        email
    )


def send_vk_account_linked_message(email: str, username: str):
    """Sends auth service VK account linked message to an email."""
    return _send_message(
        "VK account linked", 
        f"Hello, {username}! Your account was linked to external VK social account!", 
        email
    )


def send_vk_account_unlinked_message(email: str, username: str):
    """Sends auth service VK account unlinked message to an email."""
    return _send_message(
        "VK account unlinked", 
        f"Hello, {username}! Your external service VK social account was unlinked from account!", 
        email
    )