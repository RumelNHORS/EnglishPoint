from django.shortcuts import render
from rest_framework import generics, status
from api import models as api_model
from api import serializers as api_serializer
from rest_framework.permissions import AllowAny


class HeroSectionListCreateView(generics.ListCreateAPIView):
    queryset = api_model.HeroSection.objects.all()
    serializer_class = api_serializer.HeroSectionSerializer
    permission_classes = [AllowAny]

class HeroSectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = api_model.HeroSection.objects.all()
    serializer_class = api_serializer.HeroSectionSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]


class HeroImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = api_model.HeroImage.objects.all()
    serializer_class = api_serializer.HeroImageSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        hero_section = api_model.HeroSection.objects.first()
        serializer.save(hero_section=hero_section)


class HeroImageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = api_model.HeroImage.objects.all()
    serializer_class = api_serializer.HeroImageSerializer
    lookup_field = 'id'  
    permission_classes = [AllowAny]


class AboutUsListCreateAPIView(generics.ListCreateAPIView):
    queryset = api_model.AboutUs.objects.all()
    serializer_class = api_serializer.AboutUsSerializer
    permission_classes = [AllowAny]


class AboutUsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = api_model.AboutUs.objects.all()
    serializer_class = api_serializer.AboutUsSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
        

class OfferSectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = api_model.OfferSection.objects.all()
    serializer_class = api_serializer.OfferSectionSerializer
    permission_classes = [AllowAny]

class OfferSectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = api_model.OfferSection.objects.all()
    serializer_class = api_serializer.OfferSectionSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]


# List and Create OurServices
class OurServicesListCreateView(generics.ListCreateAPIView):
    queryset = api_model.OurServices.objects.all()
    serializer_class = api_serializer.OurServicesSerializer
    permission_classes = [AllowAny]

# Retrieve, Update, and Delete OurServices
class OurServicesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = api_model.OurServices.objects.all()
    serializer_class = api_serializer.OurServicesSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]


# List and Create views for Course
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = api_model.Course.objects.all()
    serializer_class = api_serializer.CourseSerializer
    permission_classes = [AllowAny]

# Retrieve, Update, and Delete views for Course
class CourseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = api_model.Course.objects.all()
    serializer_class = api_serializer.CourseSerializer
    lookup_field = 'id' 
    permission_classes = [AllowAny]
