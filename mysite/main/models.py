import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser, CustomUserManager


   # you can add more fields here.
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
    time_created = models.DateTimeField(default=timezone.now)
    time_public = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    # split categories and concepts by " "
    categories = models.CharField(max_length=100)
    concepts = models.CharField(max_length=100)
    url_path = models.TextField(default="Nothing")
    images_count = models.IntegerField(default=0)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='pdf_users')

class Thread(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Comment(models.Model):
    anonymous = models.BooleanField()
    # author_id = models.ForeignKey(User, related_name="comments_author")
    # what area the comment relates to => ideally use OCR to understand the text of the Images
    related_concept = models.TextField(default="Nothing")
    # where comment is located on the pdf
    x, y = models.IntegerField(default=0), models.IntegerField(default=0)
    time_created = models.DateTimeField(default=timezone.now)
    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_author')
    pdf = models.ForeignKey(PDF, on_delete=models.CASCADE)
    parent_thread_id = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comment_thread_id')
    text = models.TextField()
    responding_to = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comment_responding_to')
