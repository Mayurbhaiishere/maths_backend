from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('questions/', views.question_create, name='question_create'),
    path('results/', views.get_results, name='get_results'),
    path('verify_answer/', views.verify_answer, name='verify_answer'),
]

