from django.urls import path
from users.views import *


urlpatterns = [
    path('', UserListView.as_view(),name="users_list"),
    path('delete/<int:pk>', UserDeleteView.as_view(), name='user_delete'),
    path('edit/<int:pk>', UserUpdateView.as_view(), name='user_edit'),
    path('add/', UserCreateView.as_view(), name='user_add'),
]
