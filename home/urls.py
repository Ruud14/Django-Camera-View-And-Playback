from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
]