from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CandidateCareerSchool, CandidateRequest, CandidateTest
from interns.models import InternCase
from users.models import InternshipState

User = get_user_model()


@receiver(post_save, sender=CandidateRequest)
def update_user_internship_request_stage(sender, instance, **kwargs):
    """Update user internship REQUEST stage."""
    # Update user.state.request_status on CandidateRequest post_save signal
    if instance.user.state.stage == InternshipState.Stage.REQUEST:
        instance.user.state.request_status = instance.status
        # Move user to next SCHOOL stage if candidate request was accepted
        if instance.status == CandidateRequest.Status.ACCEPTED:
            # Update user state
            instance.user.state.stage = InternshipState.Stage.SCHOOL
            instance.user.state.school_status = 0
            # Create CandidateCareerSchool object
            mock_url = "https://talent.mos.ru/internships/"
            CandidateCareerSchool.objects.create(user=instance.user,
                                                 url=mock_url)
        instance.user.state.save()


@receiver(post_save, sender=CandidateCareerSchool)
def update_user_internship_school_stage(sender, instance, **kwargs):
    """Update user internship SCHOOL stage."""
    # Update user.state.school_status on CandidateCareerSchool post_save signal
    if instance.user.state.stage == InternshipState.Stage.SCHOOL:
        instance.user.state.school_status = instance.progress
        # Move user to next TEST stage if career school progress acheived
        if instance.progress == 100:
            # Update user state
            instance.user.state.stage = InternshipState.Stage.TEST
            instance.user.state.test_status = CandidateTest.Status.WAITING
            # Create CandidateTest object
            mock_url = "https://mguu.ru/test/kto-ya-v-pravitelstve-moskvy/"
            CandidateTest.objects.create(user=instance.user, url=mock_url)
        instance.user.state.save()


@receiver(post_save, sender=CandidateTest)
def update_user_internship_test_stage(sender, instance, **kwargs):
    """Update user internship TEST stage."""
    # Update user.state.test_status on CandidateTest post_save signal
    if instance.user.state.stage == InternshipState.Stage.TEST:
        instance.user.state.test_status = instance.status
        # Move user to next CASE stage if test passed
        if instance.status == CandidateTest.Status.PASS:
            # Update user role and state
            instance.user.role = User.Role.INTERN
            instance.user.save()
            instance.user.state.stage = InternshipState.Stage.CASE
            instance.user.state.case_status = InternCase.Status.WAITING
            # Create InternCase object
            mock_name = "Mock name"
            mock_description = "Mock description"
            InternCase.objects.create(
                user=instance.user,
                name=mock_name,
                description=mock_description,
            )
        instance.user.state.save()
