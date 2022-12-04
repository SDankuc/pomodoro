from rest_framework import serializers
from timetracker.models import Schema,Pomodoro,Category

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