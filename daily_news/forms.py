from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['written_date', "writer"]
        labels = {
            "title_1_en" : "First Article Title(EN)",
            "title_2_en" : "Second Article Title(EN)",
            "title_3_en" : "Third Article Title(EN)",
            "title_1_kr" : "First Article Title(KR)",
            "title_2_kr" : "Second Article Title(KR)",
            "title_3_kr" : "Third Article Title(KR)",
            "content_1_en" : "First Article Contents(EN)",
            "content_2_en" : "Second Article Contents(EN)",
            "content_3_en" : "Third Article Contents(EN)",
            "content_1_kr" : "First Article Contents(KR)",
            "content_2_kr" : "Second Article Contents(KR)",
            "content_3_kr" : "Third Article Contents(KR)",
        }

    