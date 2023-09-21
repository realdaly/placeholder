from .models import General, Page, Social_Item

def custom_context(request):
    social_items = Social_Item.objects.filter(is_active=True).order_by("order")
    website_config = General.objects.first()
    pages = Page.objects.filter(is_active=True).order_by("order")

    return {
        "social_items": social_items,
        "website_config": website_config,
        "pages": pages
    }