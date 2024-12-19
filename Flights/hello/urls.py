from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("loginPage", views.loginPage, name="loginPage"),
    path("logoutPage", views.logoutPage, name="logoutPage"),
    path("register", views.register, name="register"),
    path("flights", views.flights, name="flights"),
]

urlpatterns += staticfiles_urlpatterns()
