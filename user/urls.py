from django.urls import path
from . import views
from django.contrib.auth import views as log_views
urlpatterns = [
    path('', views.home, name='dashboard'),
    path('register/', views.userRegister, name='register'),
    path('login/', log_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', log_views.LogoutView.as_view(template_name='user/logout.html'), name='logout')
]
