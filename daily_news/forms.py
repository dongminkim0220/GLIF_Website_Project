from django import forms

class PostForm(forms.Form):

    class Meta():
        Model = Post

    