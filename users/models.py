from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# Basic User Model
class CustomUser(AbstractUser):
    # user type init
    is_glifer = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)

    email= models.EmailField(max_length = 250)
    
    def __str__(self):
        return self.username
    
# Glifer Model
## Setup

class Nth(models.Model):
    nth = models.CharField(max_length = 10)

    def __str__(self):
        return self.nth

## Model
class Glifer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True)
    is_mentor = models.BooleanField(default=False)
    is_authorized = models.BooleanField(default = False)
    name_en = models.CharField(max_length = 250)
    name_kr = models.CharField(max_length = 250)
    birthdate = models.DateField(default = "2000-01-01")
    phonenumber = models.CharField(max_length = 250)
    work_at = models.CharField(max_length = 250, blank = True)
    self_intro = models.TextField(max_length = 1000)
    profile_img = models.FileField(upload_to = 'profiles/%Y/%m/%d/', default = '/users/man-user.png')
    nth = models.ForeignKey(Nth, on_delete = models.CASCADE, primary_key = False, null = True)
    priority = models.IntegerField(default = 1)


    def __str__(self):
        return str(self.nth) + " " + self.name_kr
    

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

    def __str__(self):
        return self.subject

## Applicant Model
class Applicant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True)

    # Personal Info
    name_kr = models.CharField(max_length = 250, blank = True)
    phonenumber = models.CharField(max_length = 250, blank = True)
    birthdate = models.DateField(null = True, blank = True)
    
    # Academic Info
    stu_id = models.CharField(max_length = 50, blank = True)
    schyr = models.CharField(
        max_length=50,
        choices=schyr_CHOICES,
        default=schyr_22,
    )
    grad = models.DateField(null = True, blank = True)

    # Extracurricular Activities
    extra = models.TextField(max_length = 5000, blank = True)
    testprep = models.CharField(max_length = 1000, blank = True)
    willyou = models.CharField(max_length = 100, blank = True)
    millitary = models.CharField(max_length = 100, blank = True)
    havetaken_courses = models.ManyToManyField(Subject, related_name = "havetaken_courses_applicant", blank = True) 
    willtake_courses = models.ManyToManyField(Subject, related_name = "willtake_courses_applicant", blank = True) 

    # Essay
    glifmotive = models.TextField(max_length = 5000, blank = True)
    futureplan = models.TextField(max_length = 5000, blank = True)

    def __str__(self):
        return self.user.username
