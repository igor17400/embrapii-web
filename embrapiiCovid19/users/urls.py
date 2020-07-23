from django.urls import path 

from .views import UserListView, UserDetailView, UserCreate, UserEdit, UserDelete

urlpatterns = [
    path('users/delete/<int:id>', UserDelete, name="user_delete"),
    path('users/edit/<int:id>', UserEdit, name="user_edit"),
    path('users/new/', UserCreate, name='user_new'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('', UserListView.as_view(), name='home')
]
