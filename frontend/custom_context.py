from .models import *

def custom_context(request):
    social_items = Social_Item.objects.all()
    general_settings = General.objects.all()

    return {
        'social_items': social_items,
        'general_settings': general_settings
    }