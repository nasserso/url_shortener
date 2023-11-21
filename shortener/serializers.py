from rest_framework import serializers
from shortener.models import Shortener


class ShortnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ["slang", "original_link", "access_counter"]


class ShortnerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = [
            "original_link",
        ]
