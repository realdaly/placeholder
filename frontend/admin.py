from django.contrib import admin
from .models import *

class MainSliderAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")


# Register your models here.
admin.site.register(Image)
admin.site.register(Social_Item)
admin.site.register(General)
admin.site.register(Main_Slider, MainSliderAdmin)
