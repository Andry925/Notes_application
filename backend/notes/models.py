from django.db import models
from django.conf import settings
from category.models import Category


class Note(models.Model):
    notes_text = models.TextField(max_length=1024)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notes')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='notes_category',
        blank=True,
        null=True)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.notes_text}'
