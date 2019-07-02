from django.db import models

# Create your models here.
class Recruiting(models.Model):
    title = models.CharField(max_length = 250)
    content = models.CharField(max_length = 250)
    requirements = models.CharField(max_length = 250)
    deadline_date = models.CharField(max_length = 250)
    interview_date = models.CharField(max_length = 250)
    opensession_date = models.CharField(max_length = 250)