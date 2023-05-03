from rest_framework import serializers
from utils.models import Images


class ListImageSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        if obj.image:
            return Images.get_url(obj.image.url)
        return None
    class Meta:
        model = Images
        fields = '__all__'


class CreateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('title' , 'image')

    
