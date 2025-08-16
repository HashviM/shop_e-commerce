from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # Home page
    path("shop/", include("shop.urls")),
    path("tailoring/", include("tailoring.urls")),
    path("gallery/", include("gallery.urls")),
    path("", include("core.urls")),
    path("orders/", include("orders.urls")),
]
