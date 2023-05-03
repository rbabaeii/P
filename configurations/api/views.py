from rest_framework import generics
from configurations.models import Configure
from .serializers import ConfigureSerializer


class ConfigurationView(generics.ListAPIView):
    queryset = Configure.objects.all()
    serializer_class = ConfigureSerializer
