

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.student_view, name = "student_form"),
    path("student_data/", views.student_data, name = "student_Data"),
    path("delete/<int:id>", views.student_delete, name = "student-delete"),
    path("data/<int:id>", views.single_view, name = "single-data"),
    path("update/<int:id>", views.update_data, name = "update-data"),
]
