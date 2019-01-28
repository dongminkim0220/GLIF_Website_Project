from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# Basic User Model
class CustomUser(AbstractUser):
    # user type init
    is_glifer = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
# Glifer Model
## Setup
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

## Model
class Glifer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True)
    is_mentor = models.BooleanField(default=False)
    name_en = models.CharField(max_length = 250)
    name_kr = models.CharField(max_length = 250)
    birthdate = models.DateField(default = "2000-01-01")
    phonenumber = models.CharField(max_length = 250)
    email= models.EmailField(max_length = 250)
    work_at = models.CharField(max_length = 250, blank = True)
    self_intro = models.TextField(max_length = 1000)
    profile_img = models.FileField(upload_to = 'profiles/%Y/%m/%d/', blank = True)
    nth = models.CharField(
        max_length=2,
        choices=nth_CHOICES,
        default=glif_4th,
    )
    def __str__(self):
        return self.nth + " " + self.name_kr


# Applicant Model

## setup
schyr_11 = '1학년 1학기'
schyr_12 = '1학년 2학기'
schyr_21 = '2학년 1학기'
schyr_22 = '2학년 2학기'
schyr_31 = '3학년 1학기'
schyr_32 = '3학년 2학기'
schyr_41 = '4학년 1학기'
schyr_42 = '4학년 2학기'
schyr_etc = '기타'
schyr_CHOICES = (
    (schyr_11, '1학년 1학기'),
    (schyr_12, '1학년 2학기'),
    (schyr_21, '2학년 1학기'),
    (schyr_22, '2학년 2학기'),
    (schyr_31, '3학년 1학기'),
    (schyr_32, '3학년 2학기'),
    (schyr_41, '4학년 1학기'),
    (schyr_42, '4학년 2학기'),
    (schyr_etc, '기타'),
)

class Subject(models.Model):
    sbj_1 = 'Asset Pricing'
    sbj_2 = 'Financial Economics'
    sbj_3 = 'Financial Derivatives'
    sbj_4 = 'Money and Banking'
    sbj_5 = 'Financial Management(재무관리)'
    sbj_6 = 'Introduction to Financial Accounting(회계원리)'
    schyr_etc = '기타'
    sbj_CHOICES = (
    (sbj_1, 'Asset Pricing'),
    (sbj_2, 'Financial Economics'),
    (sbj_3, 'Financial Derivatives'),
    (sbj_4, 'Money and Banking'),
    (sbj_5, 'Financial Management(재무관리)'),
    (sbj_6, 'Introduction to Financial Accounting(회계원리)'),   
    )

    subject = models.CharField(
        max_length=50,
        choices=sbj_CHOICES,
    )

## Applicant Model
class Applicant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True)

    # Personal Info
    name_kr = models.CharField(max_length = 250)
    phonenumber = models.CharField(max_length = 250)
    birthdate = models.DateField(default = "2000-01-01")
    email= models.EmailField(max_length = 250)
    
    # Academic Info
    stu_id = models.CharField(max_length = 50)
    schyr = models.CharField(
        max_length=50,
        choices=schyr_CHOICES,
        default=schyr_22,
    )
    grad = models.DateField(default = "2020-01-01")

    # Extracurricular Activities
    extra = models.TextField(max_length = 5000)
    testprep = models.CharField(max_length = 1000)
    willyou = models.CharField(max_length = 100)
    millitary = models.CharField(max_length = 100)
    havetaken_courses = models.ManyToManyField(Subject, related_name = "havetaken_courses_applicant") 
    willtake_courses = models.ManyToManyField(Subject, related_name = "willtake_courses_applicant") 

    # Essay
    glifmotive = models.TextField(max_length = 5000)
    futureplan = models.TextField(max_length = 5000)

    def __str__(self):
        return self.user.username
