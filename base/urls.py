from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'home' ),
    
    # user-group routes
    path('user-group/', views.user_group, name='user-group'),
    path('create-user-group/', views.create_user_group, name='create-user-group'),
    path('group/<str:pk>/', views.group, name='group'),
    path('delete-group/<str:pk>/', views.delete_group, name='delete-group'),
    path('edit-group/<str:pk>/', views.edit_group, name='edit-group'),
    
    
    # category routes
    path('categories/', views.category , name='categories'),
    path('create-category/', views.create_category , name='create-category'),
    path('edit-category/<str:pk>/', views.edit_category , name='edit-category'),
    path('delete-category/<str:pk>/', views.delete_category , name='delete-category'),
    
    
    # files routes
    path('files/', views.files, name='files'),
    path('upload-file/', views.upload_file, name='upload-file'),
    path('download-file/<int:file_id>/', views.download_file, name='download-file'),
    path('delete-file/<int:file_id>/', views.delete_file, name='delete-file'),
    path('approve-file/<int:file_id>/', views.approve_file, name='approve-file'),
    path('file/<int:file_id>/', views.file, name='file'),
    path('file-remove-group/<int:file_id>/<int:group_id>/', views.file_remove_group, name='file-remove-group'),
]
