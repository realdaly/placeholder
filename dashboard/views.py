from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Count

from frontend.models import *
from .forms import *

# Create your views here.
def index(request):
    media_path = request.build_absolute_uri("/media/")
    configurations = General.objects.first()
    social_items = Social_Item.objects.all().order_by("order")

    # Query the existing types and exclude them from choices
    existing_types = Social_Item.objects.values('type').annotate(count=Count('type'))
    choices = [(item, item) for item in social_list if item not in [e['type'] for e in existing_types if e['count'] > 0]]

    has_choice = bool(choices)

    if request.method == "POST":
        general_form = GeneralForm(request.POST, instance=configurations)

        if general_form.is_valid():
            general_form.save()
            return redirect("dashboard:index")
        else:
            message = "البيانات غير صالحة"

    context = {
        "configurations":configurations,
        "media_path":media_path, 
        "social_items":social_items,
        "choices": choices,
        "has_choice": has_choice,
    }

    return render(request, "dashboard/index.html", context)




def images(request):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

    if is_ajax:
        if request.method == "GET":
            images = list(Image.objects.all().values())
            
            return JsonResponse({"context": images})
        return JsonResponse({"status": "Invalid request"}, status=400)




# social items crud
def createSocialItem(request):
    if request.method == "POST":
        type = request.POST["type"]
        link = request.POST["link"]
        order = request.POST["order"]

        is_active = request.POST["is_active"]
        if is_active == "on":
            is_active = True
        else:
            is_active = False

        Social_Item.objects.create(
            type=type,
            link=link,
            order=order,
            is_active=is_active,
        )
        return redirect("dashboard:index")
    else:
        return redirect("dashboard:index")


def editSocialItem(request, pk):
    social_item = Social_Item.objects.get(id=pk)

    if request.method == "POST":
        social_itemForm = Social_ItemForm(request.POST, instance=social_item)

        if social_itemForm.is_valid():
            social_itemForm.save()
            print(social_item.is_active)
            return redirect("dashboard:index")
        else:
            return redirect("dashboard:index")

def deleteSocialItem(request, pk):
    social_item = Social_Item.objects.get(id=pk)

    social_item.delete()
    return redirect("dashboard:index")




# pages crud
def page_items(request, slug):
    page = Page.objects.get(slug=slug)
    if(page.type == "news" or page.type == "product" or page.type == "announcement" or page.type == "post"):
        items = page.posts.all().select_related("main_img").only("title", "date", "is_active", "main_img__image")

    context = {
        "items": items,
        "page": page,
    }

    return render(request, "dashboard/pages/items.html", context)


def subpage_items(request, slug, pk):
    page = Page.objects.get(slug=slug)
    subpage = page.sub_pages.get(id=pk)
    
    items = subpage.posts.all().select_related("main_img").only("title", "date", "is_active", "main_img__image")

    context = {
        "items": items,
        "page": page,
        "subpage":subpage,
    }

    return render(request, "dashboard/pages/items.html", context)


def add_page_item(request, slug):
    page = Page.objects.get(slug=slug)

    context = {
        "page": page,
    }

    return render(request, "dashboard/pages/add.html", context)