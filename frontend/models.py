from django.db import models
from django.utils import timezone

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
    is_active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)



class Page(models.Model):
    PAGE_CHOICES = [
        ("news", "خبر"),
        ("product", "منتج"),
        ("announcement", "إعلان"),
        ("post", "منشور")
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=False)
    order = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=20, choices=PAGE_CHOICES, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)
    is_nav = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    


class SubPage(models.Model):
    page = models.ForeignKey(Page, null=True, blank=True, on_delete=models.CASCADE, related_name="sub_pages")
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    is_nav = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    


class Post(models.Model):
    TAG_CHOICES = [
        ("news", "خبر"),
        ("activity", "نشاط")
    ]
    page = models.ForeignKey(Page, blank=False, on_delete=models.CASCADE, related_name="posts")
    sub_page = models.ForeignKey(SubPage, null=True, blank=True, on_delete=models.CASCADE, related_name="posts")
    tag = models.CharField(max_length=20, choices=TAG_CHOICES, null=True, blank=True, default=TAG_CHOICES[0][0])
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=10000)
    more_info = models.CharField(max_length=255, null=True, blank=True)
    main_img = models.ForeignKey(Image, blank=False, on_delete=models.PROTECT, related_name="posts")
    order = models.PositiveIntegerField(default=0)
    date = models.DateField(default=timezone.now, editable=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.tag})"
    
    @property
    def arabic_tag(self):
        return dict(self.TAG_CHOICES).get(self.tag, "")
