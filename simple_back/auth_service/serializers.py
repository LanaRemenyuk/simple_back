from djoser.serializers import UserCreateSerializer, UserSerializer

from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'first_name', 'last_name', 'password')


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        email = serializers.EmailField()
        model = CustomUser
        fields = ('email', 'id', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = super(CustomUserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance: CustomUser, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)