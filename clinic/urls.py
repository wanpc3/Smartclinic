from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
    path('medicine/view<int:pk>/', views.view_user_medicine, name='view_user_medicine'),
    path('medicine/edit/<int:pk>/', views.edit_user_medicine, name='edit_user_medicine'),
    path('medicine/delete/<int:pk>/', views.delete_user_medicine, name='delete_user_medicine'),
    path('sign_out/', views.sign_out, name='sign_out'),
]