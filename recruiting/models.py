from django.db import models

# Create your models here.
class Applicant(models.Model):
    name = models.CharField(max_length = 250)
    date_of_birth = models.CharField(max_length = 50)
    password = models.CharField(max_length = 6)

    def __str__(self):
        return self.name
    
# class ApplicantInfo(models.Model):
#     applicant = models.ForeignKey(Applicant, on_delete = models.CASCADE, related_name= "applicant")
    
#     # Personal

#     # name
#     birthdate = models.DateField(default = "2000-01-01")
#     phonenumber = models.CharField(max_length = 250)
#     self_intro = models.TextField(max_length = 1000)
#     email = models.EmailField(max_length = 250)

#     # Academic
#     studentid = models.CharField(max_length = 50)

#     schyr_CHOICES = (
#         (1, '1학년'),
#         (2, '2학년'),
#         (3, '3학년'),
#         (4, '4학년'),
#         (0, '기타'),
#     )
    
#     schsem_CHOICES = (
#         (1, '1학기'),
#         (2, '2학기'),
#         (0, '기타'),
#     )

#     schyr = models.CharField(
#         max_length=10,
#         choices=schyr_CHOICES,
#         default= 1,
#     )

#     schsem = models.CharField(
#         max_length=10,
#         choices=schyr_CHOICES,
#         default= 1,
#     )

    

#     schyr_grad = models.CharField(max_length = 250)

#     # ExtraCurricular
#     extracurr = models.TextField(max_length= 5000)

#     # Others
#     testprep = models.TextField(max_length= 1000)
#     willyou = models.CharField(max_length = 50)
#     millitary = models.CharField(max_length = 50)
#     # taken_course = 
#     # will_take_course = 

#     # Writings
#     glifmotive = models.TextField(max_length=5000)
#     futureplan = models.TextField(max_length=5000)