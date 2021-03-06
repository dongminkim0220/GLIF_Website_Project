from django.db import models
from users.models import Glifer
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 250)
    attached_file = models.FileField(upload_to = 'resume_coaching_attached_files/%Y/%m/%d/', blank = True, null = True)
    written_date = models.DateField(auto_now = True)
    writer = models.ForeignKey(Glifer, on_delete = models.CASCADE, related_name = "resume_coaching_writer")
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resume_coaching-detail', kwargs = {'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    writer = models.ForeignKey(Glifer, on_delete = models.CASCADE, related_name = "resume_coaching_comment_writer")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
