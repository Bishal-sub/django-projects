from . import views
from django.urls import path

urlpatterns = [
    
   path('',views.home,name='homepage'),
   path('<int:pk>/',views.bookdetails,name='bookdetails'),
   path('store/',views.book_store,name='book_store')
]
