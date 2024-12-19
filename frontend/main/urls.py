from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.fetch_data, name="fetch_data"),
    path("add/", views.post_data, name="post_data"),
]
