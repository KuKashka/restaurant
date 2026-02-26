from django.urls import path
from . import views

urlpatterns = [
    # Визнач тут свої URL-шляхи
    path('', views.home, name='home'),
    path('add_to_order/<int:dish_id>/', views.add_to_order, name='add_to_order'),
    path('cart/', views.view_cart, name='view_cart'),
]