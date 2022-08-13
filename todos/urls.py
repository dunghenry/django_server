from django.urls import re_path as url, path
from todos import views
urlpatterns = [
    # url(r'^api/todos$', views.todo_list, name='todo_list'),
    # url(r'^api/todos/(?P<pk>[0-9]+)$', views.todo_detail, name='todo_detail'),
    path('api/todos', views.todo_list),
    path('api/todos/<int:id>', views.todo_detail),
]
