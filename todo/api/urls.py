# todo/api/urls.py : API urls.py
from django.conf.urls import url
from django.urls import path, include

from .views import (
    TodoListApiView,
    TodoDetailApiView
)

urlpatterns = [
    path('task-list/', TodoListApiView.as_view(),name="task_list"),
    path('task-detail/<int:todo_id>/', TodoDetailApiView.as_view(),name="task_detail"),
]