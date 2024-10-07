
from django.contrib import admin
from django.urls import path
from myform import views

urlpatterns = [
    path("", views.home_view, name='index_view'),  # For root URL
    path("form/", views.home_view, name='index_view_form'),  
    path("data/", views.data_view, name='data_view') ,
    path("admin/", admin.site.urls),
    
]
