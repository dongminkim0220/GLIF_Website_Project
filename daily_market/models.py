from django.db import models
from users.models import CustomUser
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    # General Info
    title = models.CharField(default = "Daily Market Analysis", max_length = 50)
    attached_file = models.FileField(upload_to = 'Daily_Market_attached_files/%Y/%m/%d/', blank = True, null = True)
    written_date = models.DateField(auto_now = True)
    writer = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = "Daily_Market_writer")

    # Dataset , max_digits = 10

    ## ex , max_digits = 10r
    e_u_cl = models.DecimalField(decimal_places = 2, blank = True , max_digits = 10)
    e_u_ch = models.DecimalField(decimal_places = 2, blank = True , max_digits = 10)
    u_k_cl = models.DecimalField(decimal_places = 2, blank = True , max_digits = 10)
    u_k_ch = models.DecimalField(decimal_places = 2, blank = True , max_digits = 10)

    ## bon , max_digits = 10d
    fed_cl = models.DecimalField(decimal_places = 2, blank = True , max_digits = 10)
    fed_ch = models.DecimalField(decimal_places = 2, blank = True , max_digits = 10)
    spread_cl = models.DecimalField(decimal_places = 2, blank = True , max_digits = 10)
    spread_ch = models.DecimalField(decimal_places = 2, blank = True , max_digits = 10)
    usyr2_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    usyr2_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    usyr10_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    usyr10_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    bok_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    bok_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    kryr3_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    kryr3_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    kryr10_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    kryr10_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)

    ## stock
    dj_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    dj_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    sp_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    sp_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    nas_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    nas_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    ksp_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    ksp_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    ksd_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    ksd_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    nik_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    nik_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    hk_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    hk_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)

    ## Commodity
    bco_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    bco_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    wti_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    wti_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    gd_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    gd_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)

    ## etc
    bdi_cl = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)
    bdi_ch = models.DecimalField(decimal_places = 2, blank = True, max_digits = 10)

    def __str__(self) :
        return self.title