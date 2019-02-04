from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['written_date', "writer"]
        labels = {
        'title': "",
        'e_u_cl': "", 'e_u_ch': "",
        'u_k_cl': "", 'u_k_ch': "",
        'fed_cl': "", 'fed_ch': "",
        'spread_cl': "", 'spread_ch': "",
        'usyr2_cl': "", 'usyr2_ch': "",
        'usyr10_cl': "", 'usyr10_ch': "",
        'bok_cl': "", 'bok_ch': "",
        'kryr3_cl': "", 'kryr3_ch': "",
        'kryr10_cl': "", 'kryr10_ch': "",
        'dj_cl': "", 'dj_ch': "",
        'sp_cl': "", 'sp_ch': "",
        'nas_cl': "", 'nas_ch': "",
        'ksp_cl': "", 'ksp_ch': "",
        'ksd_cl': "", 'ksd_ch': "",
        'nik_cl': "", 'nik_ch': "",
        'hk_cl': "", 'hk_ch': "",
        'bco_cl': "", 'bco_ch': "",
        'wti_cl': "", 'wti_ch': "",
        'gd_cl': "", 'gd_ch': "",
        'bdi_cl': "", 'bdi_ch': "", 
        }
