from django.contrib import admin
from django.urls import path
from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.sign_up, name="signup"),
    path("login/", views.login_view, name="login-view"),
    path("password1/", views.passwordchangeview1, name="passwordchange1-view"),
    path("password2/", views.passwordchangeview2, name="passwordchange2-view"),
    path("profile/", views.user_profile, name="user-profile-view"),
]
