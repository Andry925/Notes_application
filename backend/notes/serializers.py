from rest_framework import serializers
from .models import Note
from .models import Category


class NoteSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Note
        fields = ('category', 'notes_text', 'is_archived')

    def create(self, validated_data):
        current_user = self.context.get('current_user')
        filter_criteria = validated_data.get('category').get('name')
        category_obj = Category.objects.get(name=filter_criteria, owner=current_user)
        note = Note.objects.create(
            category=category_obj,
            is_archived=validated_data.get('is_archived'),
            notes_text=validated_data.get('notes_text'),
            owner=current_user)
        return note
