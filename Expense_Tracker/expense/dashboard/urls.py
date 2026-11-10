
from django.urls import path
from . import views
urlpatterns = [
    path('',views.expense,name='expense'),
    path('create_expense/',views.create_expense,name="create_expense"),
    path('update_expesne/<int:id>',views.update_expesne,name="update_expesne"),
    path('delete_expense/<int:id>',views.delete_expense,name="delete_expense"),

    
]
