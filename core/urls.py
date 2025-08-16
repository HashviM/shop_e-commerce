from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
]
