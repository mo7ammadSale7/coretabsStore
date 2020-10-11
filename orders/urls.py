from django.urls import path
from .views import add_to_order

urlpatterns = [
    path('', add_to_order, name="add_to_order"),

]
