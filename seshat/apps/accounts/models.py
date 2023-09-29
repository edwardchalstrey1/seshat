from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.core.exceptions import ValidationError
from .custom_validators import validate_email_with_dots  # Import your custom validator
from django.core.validators import EmailValidator



# class CustomUser(AbstractUser):
#     email = models.EmailField(
#         unique=True,  # Make sure emails are unique
#         validators=[validate_email_with_dots, EmailValidator(message="Enter a valid email address.")],
#     )

class Profile(models.Model):
    SESHATADMIN = 1
    RA = 2
    SESHATEXPERT = 3
    PUBLICUSER = 4
    ROLE_CHOICES = (
        (SESHATADMIN, 'Seshat Admin'),
        (RA, 'Research Assistant'),
        (SESHATEXPERT, 'Seshat Expert'),
        (PUBLICUSER, 'Public User'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False, null=True, blank=True)
    #avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField( null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('user-profile')

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Seshat_Expert(models.Model):
    SESHATADMIN = 'Seshat Admin'
    RA = 'RA'
    SESHATEXPERT = 'Seshat Expert'
    ROLE_CHOICES = (
        (SESHATADMIN, 'Seshat Admin'),
        (RA, 'RA'),
        (SESHATEXPERT, 'Seshat Expert'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=60,
        choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + " " + self.user.last_name
        else:
            return self.user.username + " (" + self.role + ")"

class Seshat_Task(models.Model):
    giver = models.ForeignKey(Seshat_Expert, on_delete=models.CASCADE)
    taker = models.ManyToManyField(Seshat_Expert, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)ss", blank=True,)
    task_description = models.TextField( null=True, blank=True)
    task_url = models.URLField(max_length=200, null=True, blank=True)


    def get_absolute_url(self):
        return reverse('seshat_task-detail', args=[str(self.id)])
    
    @property
    def display_takers(self):
        all_takers = []
        for taker in self.taker.all():
            all_takers.append(taker.__str__())
        return "<br>".join(all_takers)

    @property
    def clickable_url(self):
        return f'<a href="{self.task_url}">{self.task_url}</a>'

    def __str__(self):  # __unicode__ for Python 2
        return self.giver.user.username + " has a atsk for you: " +  self.task_description
