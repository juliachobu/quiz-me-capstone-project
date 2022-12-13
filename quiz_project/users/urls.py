from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/<str:username>/', views.UserProfileView.as_view(), name='profile'),

]