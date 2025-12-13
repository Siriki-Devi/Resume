from django.urls import path
from . import views

urlpatterns = [
    path("", views.empform, name="empform"),
    path("api/create_emp/", views.create_emp, name="create_emp")
]
