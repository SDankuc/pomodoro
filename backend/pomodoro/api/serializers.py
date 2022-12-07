from rest_framework import serializers
from timetracker.models import Schema,Pomodoro,Category
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password", )

class SchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = [
            "id",
            "duration",
            "standard_break",
            "long_break",
            "long_break_delay",
            "auto_start_pomodoros",
            "auto_start_breaks",
            "active",
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "default"
        ]

class PomodoroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pomodoro
        fields = [
            "id",
            "category_id",
            "title",
            "amount",
            "done"
        ]

