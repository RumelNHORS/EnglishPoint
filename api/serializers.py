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


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.AboutUs
        fields = ['id', 'title', 'content', 'image']


class OfferSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.OfferSection
        fields = ['id', 'title', 'content', 'percentage', 'image', 'description', 'color']


class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.OurServices
        fields = ['id', 'title', 'content', 'link', 'image']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Course
        fields = ['id', 'title', 'description', 'image', 'link', 'duration', 'price', 'created_date', 'updated_date']
