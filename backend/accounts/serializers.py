from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

UserCustomModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustomModel
        fields = '__all__'

    def create(self, validated_data):
        user_instance = UserCustomModel.objects.create(**validated_data)
        user_instance.set_password(validated_data.get("password"))
        user_instance.save()
        return user_instance

    def validate(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        if len(password) < 8 or (len(username) < 8):
            raise ValidationError(
                "Both password and username must be 8 lenght")
        return validated_data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = UserCustomModel
        fields = ('email', 'password')

    def login_user(self, data):
        email = data.get("email")
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise ValidationError("Such user does not exist")
        return user
