from django.urls import path
from rest_framework import routers

from . import views 

router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet, basename='questions')
router.register('choices', views.ChoiceViewSet, basename='choices')
router.register('results', views.ResultViewSet, basename='results')
router.register('users', views.UserViewSet, basename='users')


urlpatterns = router.urls + [
    path('current-user/', views.CurrentUserView.as_view())
   
]