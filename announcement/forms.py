from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta():
        Model = Post
        fields = __all__