
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.addtodoitem,name='add'),
    path('completed/<todo_id>',views.completedtodo,name='completed'),
    path('deletecompleted',views.deletecompleted,name='deletecompleted'),
    path('deleteall',views.deleteAll,name='deleteall')
]
