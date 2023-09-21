from django.shortcuts import render, redirect
from django.http import JsonResponse

from frontend.models import *
from .forms import *

# Create your views here.




# -------------------------------------------- UPDATE ------------------------------------
def index(request):
    media_path = request.build_absolute_uri("/media/")
    configurations = General.objects.first()

    if request.method == "POST":
        form = GeneralForm(request.POST, instance=configurations)
        if form.is_valid():
            form.save()
            return redirect("dashboard:index")
        else:
            message = "البيانات غير صالحة"

    context = {"configurations":configurations, "media_path":media_path}

    return render(request, "dashboard/index.html", context)




def images(request):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

    if is_ajax:
        if request.method == "GET":
            images = list(Image.objects.all().values())
            
            return JsonResponse({"context": images})
        return JsonResponse({"status": "Invalid request"}, status=400)



