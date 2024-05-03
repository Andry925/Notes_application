from django.urls import path
from . import views

urlpatterns = [
    path('manage_categories/', views.ManageCategoryView.as_view(), name='categories'),
]