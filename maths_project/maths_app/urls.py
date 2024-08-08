from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    # path('questions/new', views.question_create, name='question_create'),
    # path('results/', views.put_results, name='get_results'),

]
