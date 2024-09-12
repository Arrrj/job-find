from django.db import models
from django.contrib.auth.models import AbstractUser

class UserRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    resume_upload = models.FileField(upload_to='uploads/resume')
    cover_letter = models.FileField(upload_to='uploads/coverletter')

class CustomRegistration(AbstractUser):
    pass