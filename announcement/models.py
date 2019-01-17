from django.db import models
from users.models import CustomUser
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 250)
    attached_file = models.FileField(upload_to = 'announcement_attached_files/%Y/%m/%d/', blank = True, null = True)
    written_date = models.DateField(auto_now = True)
    writer = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    content = models.TextField(max_length= 5000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'pk': self.pk})
