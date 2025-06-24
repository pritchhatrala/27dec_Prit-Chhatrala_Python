from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.get_comments),
    path('comments/add/', views.add_comment),
    path('comments/delete/<int:pk>/', views.delete_comment),
]
