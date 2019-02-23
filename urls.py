from django.urls import path

from . import views

urlpatterns = [
    path('', views.TasksAll, name='task_all'),
    path('taskdone/', views.TasksDone, name='task_done'),
    path('task/<int:pk>', views.TaskDetail.as_view(), name='task_detail'),
    path('add/', views.TaskAddForm.as_view(), name='task_add'),
    path('update/<int:pk>/', views.TaskUpdate.as_view(), name='task_update'),
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),
    path('dodone/<int:num>/', views.TaskDoDone, name='task_dodone'),
]
