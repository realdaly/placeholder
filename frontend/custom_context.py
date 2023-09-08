from .models import *

def custom_context(request):
    social_items = Social_Item.objects.all()
    general_settings = General.objects.all()
    pages = Page.objects.filter(is_active=True).order_by("order")

    return {
        "social_items": social_items,
        "general_settings": general_settings,
        "pages": pages
    }