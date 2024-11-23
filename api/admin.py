from django.contrib import admin
from api import models as api_models

# Register your models here.
admin.site.register(api_models.HeroSection)
admin.site.register(api_models.HeroImage)
admin.site.register(api_models.AboutUs)
admin.site.register(api_models.OfferSection)
admin.site.register(api_models.OurServices)
