from django.urls import path
from . import views

#urlConf
urlpatterns = [
    # path('testingPurpose/hello/', views.say_hello)
    path('hello/', views.say_hello),
    path('', views.say_hello)
]