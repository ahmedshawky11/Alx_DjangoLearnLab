from django.contrib.auth.models import User
from django.db import models

class Role(models.TextChoices):
    ADMIN = 'ADMIN'
    LIBRARIAN = 'LIBRARIAN'
    MEMBER = 'MEMBER'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.MEMBER)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

# Create user profile automatically upon user creation
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
