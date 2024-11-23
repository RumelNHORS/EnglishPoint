from django.urls import path
from api import views as api_view



urlpatterns = [
    path('hero_section/', api_view.HeroSectionListCreateView.as_view(), name='hero_section'),
    path('hero_section/<int:id>/', api_view.HeroSectionRetrieveUpdateView.as_view(), name='hero_section_update'),
    path('hero_images/', api_view.HeroImageListCreateAPIView.as_view(), name='hero_images'),
    path('hero_images/<int:id>/', api_view.HeroImageRetrieveUpdateView.as_view(), name='hero_image_update'),
]