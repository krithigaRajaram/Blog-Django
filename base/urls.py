
from django.urls import path
from . import views
urlpatterns = [
   path('create/', views.create_post, name='create_post'),
   path('search/', views.search, name='search'),
   path('<slug:slug>/', views.detail, name='post_detail'),
]