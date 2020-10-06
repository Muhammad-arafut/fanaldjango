from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('activity',views.activity, name='activity'),
    path('contact',views.contact, name='contact'),
    path('sign_up',views.sign_up, name='sign_up'),
]