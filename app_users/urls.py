from django.urls import path, include
from .views import profiles_list, profile_detail, update_profile


urlpatterns = [
    path('auth/', include('allauth.urls')),
    path('users/', profiles_list),
    path('profile/<int:pk>/', profile_detail, name='profile_url'),
    path('profile/update/', update_profile, name='update_profile_url'),
]
 