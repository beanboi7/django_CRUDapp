from django.urls import path
from blog.views import (
     BlogListView,
     BlogCreateView,
     BlogDeleteView,
     BlogDetailView,
     BlogUpdateView
)
 
urlpatterns = [
     path('', BlogListView.as_view(), name = 'home'),
     path('posts/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
     path('post/new/', BlogCreateView.as_view(), name ='post_new'),
     path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name = 'post_edit'),
     path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name = 'post_delete'),
]
 