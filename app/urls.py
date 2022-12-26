from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view()),
    path('test/',views.TestView.as_view(),name='test'),
]
