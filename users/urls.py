from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.edit, name='edit'),
    path('saveprofile/', views.save_profile, name='save_profile')
]
