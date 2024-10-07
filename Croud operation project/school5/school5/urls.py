from django.contrib import admin
from django.urls import path
from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home-view"),
    path('stu/<int:id>', views.get_student, name="student-data"),
    path('stu_delete/<int:id>', views.delete_stu, name="student-delete"),
    path('stu_update/<int:id>', views.update_student_view, name="student-update"),
]
