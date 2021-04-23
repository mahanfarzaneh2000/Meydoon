from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import ProfileEditView, profile

urlpatterns = [
    path('register', views.register, name="register"),
    path('login',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/edit', ProfileEditView.as_view(), name='editprofile'),
    path('profile', views.profile,name='profile')
]