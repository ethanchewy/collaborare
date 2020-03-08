from django.conf import settings
from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser, CustomUserManager

# Create your models here.
# class User(AbstractBaseUser):
#     YEAR_IN_SCHOOL_CHOICES = [
#         ('FR', 'Freshman'),
#         ('SO', 'Sophomore'),
#         ('JR', 'Junior'),
#         ('SR', 'Senior'),
#         ('GR', 'Graduate'),
#     ]
#     year = models.CharField(
#         max_length=2,
#         choices=YEAR_IN_SCHOOL_CHOICES,
#         default=None,
#     )
#
# class UserManager(CustomUserManager):
#
#
#
# class Student(User):
#
# class Instructor(User):

class PDF(models.Model):
    tim_created = models.DateTimeField(default=timezone.now)
    time_public = models.TimeField(auto_now=False, auto_now_add=False)
    due_date = models.TimeField(auto_now=False, auto_now_add=False)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    # split categories and concepts by " "
    categories = models.CharField(max_length=10)
    concepts = models.CharField(max_length=10)

class Comment(models.Model):
    anonymous = models.BooleanField()
    # author_id = models.ForeignKey(User, related_name="comments_author")
    time_created = models.DateTimeField(default=timezone.now)
    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_author')
    pdf = models.ForeignKey('self', on_delete=models.CASCADE)
    parent_thread_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='comment_thread_id')
    text = models.TextField()
    responding_to = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comment_responding_to')
