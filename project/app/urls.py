from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('upload/',views.upload,name='upload'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('like/<str:pk>',views.like_pic,name='like'),
    path('profile/<str:pk>',views.profile,name= 'profile'),
    path('show/<str:pk>',views.show,name='show'),
    path('login/',views.loginpage,name='login')
]