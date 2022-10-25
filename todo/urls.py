from django.urls import path
from todo.views import *

urlpatterns = [
   path('',index,name='index'),
   path('add_todo',add_todo,name='add_todo'),
   path('update_todo/<int:pk>',update_todo,name='update_todo'),
   path('delete_todo/<int:pk>',delete_todo,name='delete_todo'),
   path('completed_task',completed_task,name='completed_task'),
   path('incompleted_task',incompleted_task,name='incompleted_task'),
]
