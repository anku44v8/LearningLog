from django.urls import path,include
from . import views
app_name = 'accounts'
urlpatterns = [
    # Log in and Log out
    path('',include('django.contrib.auth.urls')),
    # Register a user
    path('register/',views.register,name='register'),
]