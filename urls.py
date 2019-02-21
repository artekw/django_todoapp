from django.urls import path

from . import views

urlpatterns = [
    path('', views.TasksAll, name='task_all'),
    #path('?cat=<category>/', views.TaskByCategoryViewList.as_view()),
    path('task/<int:pk>', views.TaskDetail.as_view(), name='task_detail'),
    path('add/', views.TaskAdd.as_view(), name='task_add'),
    path('update/<int:pk>/', views.TaskUpdate.as_view(), name='task_update'),
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),
    path('done/<int:pk>/', views.TaskDone.as_view(), name='task_done'),
]
