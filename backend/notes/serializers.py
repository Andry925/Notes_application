from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Note
        fields = ('category', 'notes_text', 'is_archived')
