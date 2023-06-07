from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('users/', views.index, name='users'),
    path('edit-user/<str:pk>', views.edit_user, name='edit-user'),
    path('delete-user/<str:pk>', views.delete_user, name='delete-user'),
    path('register-user/', views.register_user, name='register-user'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name = 'auth/login.html'
        ), name='login'),
]