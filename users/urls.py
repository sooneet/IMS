from django.urls import path,include

from . import views


urlpatterns = [
    path('login/',views.login_page,name='login'),
]