from rest_framework import serializers
from city.models import Province, City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['name']


class ProvinceSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True)

    class Meta:
        model = Province
        fields = ['name', 'cities']
