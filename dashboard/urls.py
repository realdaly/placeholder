from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="index"),
    path("images/", views.images, name="images"),

    # social items crud
    path("create-socialitem/", views.createSocialItem, name="createSocialItem"),
    path("edit-socialitem/<str:pk>/", views.editSocialItem, name="editSocialItem"),
    path("delete-socialitem/<str:pk>/", views.deleteSocialItem, name="deleteSocialItem"),

    path("<str:slug>/add/", views.add_page_item, name="addPageItem"),
    
    path("<str:slug>/", views.page_items, name="pageItems"),
    path("<str:slug>/<str:pk>/", views.subpage_items, name="subpageItems"),

]