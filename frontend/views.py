from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    sliders = Main_Slider.objects.filter(is_active=True).order_by("order")
    posts = Post.objects.filter(is_active=True).order_by("order")[:5]

    context = {
        "sliders": sliders,
        "posts": posts
    }
    return render(request, "frontend/index.html", context)