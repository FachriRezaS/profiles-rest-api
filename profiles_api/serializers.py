from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field to for testing our api view"""

    name = serializers.CharField(max_length=10)