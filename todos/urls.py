from django.urls import re_path as url
from todos import views
urlpatterns = [
    url(r'^api/todos$', views.todo_list, name='todo_list'),
]
