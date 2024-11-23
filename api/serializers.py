from rest_framework import serializers
# from .models import HeroSection, HeroImage
from api import models as api_models


class HeroImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.HeroImage
        fields = ['id', 'image', 'hero_section']


class HeroSectionSerializer(serializers.ModelSerializer):
    images = HeroImageSerializer(many=True, read_only=True)

    class Meta:
        model = api_models.HeroSection
        fields = ['id', 'title', 'description', 'button_text_primary', 'button_text_secondary', 'images']
