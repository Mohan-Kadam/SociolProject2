from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('register/',views.register, name='register'),
    path('servicepage/',views.post_service, name='postservice'),
    path('webdesign_list/',views.webdesign_list, name='webdesign_list'),
    path('videoediting_list/',views.videoediting_list, name='videoediting_list'),
    path('photoediting_list/',views.photoediting_list, name='photoediting_list'),
    path('uidesign_list/',views.uidesign_list, name='uidesign_list'),
    path('it_list/',views.it_list, name='it_list'),
    path('account_list/',views.account_list, name='account_list'),
    path('querypage/',views.queries, name='queries'),
    path('query_list/',views.query_list, name='query_list'),
    path('query_detail/<int:pk>',views.query_detail, name='query_detail'),


]




