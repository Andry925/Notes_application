from django.urls import path
from . import views

urlpatterns = [
    path('notes_operations/', views.NonPrimaryKeyNoteView.as_view(), name='notes-operation'),
    path('pk_notes_operations/<int:pk>', views.PrimaryKeyNoteView.as_view(), name='notes-operations-pk'),
    path('archived_notes/', views.ArchivedNotesView.as_view(), name='archive_notes'),
    path('filter_notes/', views.FilterNotesView.as_view(), name='filter_notes')
]