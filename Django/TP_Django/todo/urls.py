from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name='TodoList'),
     path('deleteTask/<str:pk>', views.deleteTask, name='delete_task'),
]