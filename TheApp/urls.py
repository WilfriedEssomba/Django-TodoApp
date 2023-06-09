from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('/add_task/', views.add_task, name='add_task'),
    path('/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('/<int:task_id>/update/', views.update_task, name='update_task'),
]