from django.urls import path
from . import views

urlpatterns = [
    path('notes_operations/', views.NonPrimaryKeyNoteView.as_view(), name='notes-operation')
]