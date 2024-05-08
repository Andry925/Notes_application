import re
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
    words_in_note = models.IntegerField(default=0)
    unique_words_in_note = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.words_in_note = self.calculate_words_in_note()[0]
        self.unique_words_in_note = self.calculate_words_in_note()[1]
        super().save(*args, **kwargs)

    def calculate_words_in_note(self):
        words_amount = re.findall("[a-zA-Z_]+", self.notes_text)
        unique_words_amount = set(words_amount)
        return len(words_amount), len(unique_words_amount)

    def __str__(self):
        return f'{self.notes_text}'
