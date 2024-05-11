from django.urls import path
from .views import home, redirect_to_url
urlpatterns = [
    path('',home,name='home-page'),
    path("<str:pk>/",redirect_to_url,name='redirect')
]