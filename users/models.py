from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# class User(AbstractUser):
#     is_normal_user = models.BooleanField(default = False)
#     is_glifer = models.BooleanField(default = False)
#     is_ob = models.BooleanField(default = False)
#     is_staff = models.BooleanField(default = False)
#     is_superuser = models.BooleanField(default = False)

class CustomUser(AbstractUser):
    # add additional fields in here
    name_en = models.CharField(max_length = 250)
    name_kr = models.CharField(max_length = 250)
    birthdate = models.DateField(default = "2000-01-01")
    phonenumber = models.CharField(max_length = 250)
    self_intro = models.TextField(max_length = 1000)
    workplace = models.CharField(max_length = 250, default = '')
    profile_img = models.FileField(upload_to = 'profiles/%Y/%m/%d/')

    glif_OB = 'OB'
    glif_1st = '1기'
    glif_2nd = '2기'
    glif_3rd = '3기'
    glif_4th = '4기'
    nth_CHOICES = (
        (glif_OB, 'OB'),
        (glif_1st, '1기'),
        (glif_2nd, '2기'),
        (glif_3rd, '3기'),
        (glif_4th, '4기'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=nth_CHOICES,
        default=glif_4th,
    )

    def __str__(self):
        return self.name_kr
    