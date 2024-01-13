from django.urls import path
from account.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('change/', change, name='change'),
    path('edit/', editprofile, name='editprofile'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='account/login.jinja'
    ), name='login'),
]