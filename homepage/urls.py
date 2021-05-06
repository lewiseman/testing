from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    path('', views.api_root, name="root"),
    path('home/', views.Stories.as_view(), name="home"),
    path('users/', views.UserList.as_view(),name='users'),

    path('demo/', views.DemoStories.as_view(), name="demo"),
    
    path('<pk>/', views.Story.as_view(), name="story"),
    path('user/<int:pk>/', views.UserDetail.as_view(),name='user'),
    ])
    