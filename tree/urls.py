from django.urls import path
from . import views

urlpatterns = [
    path('tree/', views.tree_list),
    # path('node/<int:pk>/', views.node_list),
]