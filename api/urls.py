from django.urls import path
from api import views as api_view



urlpatterns = [
    path('hero_section/', api_view.HeroSectionListCreateView.as_view(), name='hero_section'),
    path('hero_section/<int:id>/', api_view.HeroSectionRetrieveUpdateDestroyView.as_view(), name='hero_section_update'),
    path('hero_images/', api_view.HeroImageListCreateAPIView.as_view(), name='hero_images'),
    path('hero_images/<int:id>/', api_view.HeroImageRetrieveUpdateDestroyView.as_view(), name='hero_image_update'),
    path('about_us/', api_view.AboutUsListCreateAPIView.as_view(), name='about_us'),
    path('about_us/<int:id>/', api_view.AboutUsRetrieveUpdateDestroyView.as_view(), name='about_us_update'),
    path('offer_section/', api_view.OfferSectionListCreateAPIView.as_view(), name='offer_section_list_create'),
    path('offer_section/<int:id>/', api_view.OfferSectionRetrieveUpdateDestroyView.as_view(), name='offer_section_update'),
    path('our_services/', api_view.OurServicesListCreateView.as_view(), name='our_services_list_create'),
    path('our_services/<int:id>/', api_view.OurServicesRetrieveUpdateDestroyView.as_view(), name='our_services_retrieve_update_destroy'),
    path('courses/', api_view.CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:id>/', api_view.CourseRetrieveUpdateDeleteView.as_view(), name='course-retrieve-update-delete'),
]