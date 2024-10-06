
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home , name='homes'),
    path('login/', views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
]