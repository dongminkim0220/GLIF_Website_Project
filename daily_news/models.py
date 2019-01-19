from django.db import models
from users.models import CustomUser
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    # General Info
    title = models.CharField(default = "Daily News Clipping", max_length = 50)
    attached_file = models.FileField(upload_to = 'Daily_News_Clipping/%Y/%m/%d/', blank = True, null = True)
    written_date = models.DateField(auto_now = True)
    writer = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = "Daily_News_Clipping_writer")

    wsj = "wsj"
    ft = "ft"
    bb = "bb"
    news_CHOICES = (
        (wsj, "WSJ"),
        (ft, "FT"),
        (bb, "BB"),
    )
    news_type = models.CharField(
        max_length = 10 ,
        choices = news_CHOICES,
    )

    content_1_kr = models.TextField(max_length = 5000)
    content_2_kr = models.TextField(max_length = 5000)
    content_3_kr = models.TextField(max_length = 5000)
    content_1_en = models.TextField(max_length = 5000)
    content_2_en = models.TextField(max_length = 5000)
    content_3_en = models.TextField(max_length = 5000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('daily_news-detail', kwargs = {'pk': self.pk})

