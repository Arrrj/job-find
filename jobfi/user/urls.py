from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.userlogin,name='login'),
    path('signup/',views.userregistration,name='signup'),
    path('home/',views.home,name='home')

]