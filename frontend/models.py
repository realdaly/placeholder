from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="images", blank=False)

    def __str__(self):
        return f"{self.id}"

social_list= [
    "facebook",
    "instagram",
    "telegram",
    "twitter",
    "youtube",
    "whatsapp",
]

class Social_Item(models.Model):
    ITEM_CHOICES=sorted([(item, item) for item in social_list])

    type = models.CharField(max_length=20, choices=ITEM_CHOICES, null=True, blank=True)
    link = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.type}: {self.link}"
    
class General(models.Model):
    logo = models.ForeignKey(Image, null=True, blank=True, related_name="logo", on_delete=models.PROTECT)

class Main_Slider(models.Model):
    bg = models.ForeignKey(Image, null=True, blank=True, related_name="bg", on_delete=models.PROTECT)
    main_img = models.ForeignKey(Image, null=True, blank=True, related_name="mainSlider", on_delete=models.PROTECT)
    title = models.CharField(max_length=250, null=True, blank=True)
    body = models.CharField(max_length=1000, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)