from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail_url'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create_url'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update_url'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete_url'),
    path('about/', views.about, name='blog-about'),
]
