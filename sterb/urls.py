from django.contrib import admin
from django.urls import path, include

from sterb import views

urlpatterns = [
    path('rand/', views.randomNumber ),
    path('', views.BlogListView.as_view()),
    path('<int:pk>/', views.BlogDetailView.as_view()),
    path('createBlog/', views.BlogCreateView.as_view()),
    path('<int:pk>/updateBlog/', views.BlogUpdateView.as_view()),

]
