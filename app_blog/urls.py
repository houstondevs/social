from .views import post_list, post_detail
from django.urls import path, include


urlpatterns = [
    path('posts/', post_list, name='posts_list_url'),
    path('post/<int:pk>/', post_detail, name='post_detail_url'),
]
 