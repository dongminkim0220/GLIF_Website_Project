from django.db import models
from users.models import Glifer
from django.urls import reverse
from datetime import date

# Create your models here.
class Post(models.Model):
    # General Info
    today = str(date.today()).replace("-", "")

    title = models.CharField(default = today+ " Daily News Clipping", max_length = 50)
    written_date = models.DateField(auto_now = True)
    writer = models.ForeignKey(Glifer, on_delete = models.CASCADE, related_name = "Daily_News_Clipping_writer")

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

    title_1_kr = models.CharField(max_length = 500, blank = True, null = True)
    title_2_kr = models.CharField(max_length = 500, blank = True, null = True)
    title_3_kr = models.CharField(max_length = 500, blank = True, null = True)
    title_1_en = models.CharField(max_length = 500, blank = True, null = True)
    title_2_en = models.CharField(max_length = 500, blank = True, null = True)
    title_3_en = models.CharField(max_length = 500, blank = True, null = True)

    content_1_kr = models.TextField(max_length = 5000, blank = True, null = True)
    content_2_kr = models.TextField(max_length = 5000, blank = True, null = True)
    content_3_kr = models.TextField(max_length = 5000, blank = True, null = True)
    content_1_en = models.TextField(max_length = 5000, blank = True, null = True)
    content_2_en = models.TextField(max_length = 5000, blank = True, null = True)
    content_3_en = models.TextField(max_length = 5000, blank = True, null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('daily_news-detail', kwargs = {'pk': self.pk})

