from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import InternshipState
from candidates.models import CandidateRequest
from interns.models import InternIntro


User = get_user_model()


@receiver(post_save, sender=User)
def create_user_internship_state(sender, instance, created, **kwargs):
    """Create internship state record in database for new CANDIDATE user."""
    if (created and not instance.is_superuser
        and instance.role == User.Role.CANDIDATE):
        InternshipState.objects.create(user=instance)


@receiver(post_save, sender=CandidateRequest)
def update_user_internship_request_stage(sender, instance, **kwargs):
    """Update user internship state for REQUEST internship stage."""
    
    # Update user status on every post_save signal from CandidateRequest
    instance.user.state.request_status = instance.status
    instance.user.state.save()

    # Change user role and state if candidate request was accepted
    if (instance.status == CandidateRequest.Status.ACCEPTED
        and instance.user.role != User.Role.INTERN):
        # Update user role
        instance.user.role = User.Role.INTERN
        instance.user.save()
        # Move user to next INTRO internship stage
        instance.user.state.stage = InternshipState.Stage.INTRO
        instance.user.state.save()
        # Create InternIntro object
        mock_url = "https://talent.mos.ru/internships/"
        InternIntro.objects.create(user=instance.user, url=mock_url)
