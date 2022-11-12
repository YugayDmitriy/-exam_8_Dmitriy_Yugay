from django.urls import path
from accounts.views import signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', signup, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]