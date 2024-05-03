from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Category
        fields = "__all__"

    def validate(self, validated_data):
        category_name = validated_data.get("name")
        current_user = self.context.get('current_user')
        if Category.objects.filter(
                name=category_name,
                owner=current_user).exists():
            raise ValidationError("You already have a category with this name")
        return validated_data
