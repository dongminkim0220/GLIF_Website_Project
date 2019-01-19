from django import forms

class PostForm(forms.ModelForm):
    class Meta():
        Model = Post
        fields = __all__