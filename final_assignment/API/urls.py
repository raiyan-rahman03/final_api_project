from django.urls import path ,include
from .views import *







urlpatterns = [
    path('menu-items/<int:pk>/', menu_items_view),
    path('menu-items/', menu_items_view),
    path('group/<str:name>/',group_org),
    path('group/<str:name>/<int:id>/',delete_grp_user),
    path('cart',CartView.as_view()),
    path('cartt',CartAddView.as_view()),
   
    path('cart_del/' ,cart_del.as_view()),


]
    
    
    

