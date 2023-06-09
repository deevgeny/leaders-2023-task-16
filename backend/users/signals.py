from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import InternshipState

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_internship_state(sender, instance, created, **kwargs):
    """Create internship state record in database for new CANDIDATE user."""
    if (created and not instance.is_superuser
            and instance.role == User.Role.CANDIDATE):
        InternshipState.objects.create(user=instance)
