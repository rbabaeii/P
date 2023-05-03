from rest_framework import serializers
from configurations.models import Configure


class ConfigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configure
        fields = '__all__'
