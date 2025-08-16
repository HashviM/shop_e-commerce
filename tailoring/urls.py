from django.urls import path
from . import views

app_name = "tailoring"

urlpatterns = [
    path("", views.index, name="index"),
]
