from .serializers import ProvinceSerializer, CitySerializer
from city.models import Province, City
from rest_framework import generics


class ProvinceView(generics.ListAPIView):
    queryset = Province.objects.prefetch_related('cities').all()
    serializer_class = ProvinceSerializer


class CityView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
