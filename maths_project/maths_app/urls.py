from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('questions/<int:pk>/', views.question_detail, name='question_detail'),
    path('questions/new/', views.question_create, name='question_create'),
    path('questions/<int:pk>/answer/', views.answer_create, name='answer_create'),
]
