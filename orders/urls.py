from django.urls import path
from .views import add_to_order

urlpatterns = [
    path('orders/add/', add_to_order, name="add_to_order"),

]
