from django.shortcuts import render
from rest_framework import generics, status
from api import models as api_model
from api import serializers as api_serializer

class HeroSectionListCreateView(generics.ListCreateAPIView):
    queryset = api_model.HeroSection.objects.all()
    serializer_class = api_serializer.HeroSectionSerializer

class HeroSectionRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = api_model.HeroSection.objects.all()
    serializer_class = api_serializer.HeroSectionSerializer
    lookup_field = 'id' 


class HeroImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = api_model.HeroImage.objects.all()
    serializer_class = api_serializer.HeroImageSerializer

    def perform_create(self, serializer):
        hero_section = api_model.HeroSection.objects.first()
        serializer.save(hero_section=hero_section)


class HeroImageRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = api_model.HeroImage.objects.all()
    serializer_class = api_serializer.HeroImageSerializer
    lookup_field = 'id'    

