from django_filters import rest_framework as rest_filters

from .models import Note


class NoteFilter(rest_filters.FilterSet):
    category = rest_filters.CharFilter(
        lookup_expr='iexact',
        field_name='category__name')

    class Meta:
        model = Note
        fields = ['category']
