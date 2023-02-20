from django.urls import path
from . import views
urlpatterns =[
    path('',views.index ,name='index'),
    path('signup',views.signup ,name ='signup'),
    path('signin',views.signin ,name ='signin'),
    path('upload',views.upload , name = 'upload'),
    path('like_post',views.like_post, name = 'like_post'),
    path('follow',views.follow, name = 'follow'),
    path('logout',views.signin ,name ='logout'),
    path('settings',views.settings ,name ='settings'),
    path('profile/<str:pk>',views.profile, name = 'profile'),
    path('search',views.search ,name ='search'),
]