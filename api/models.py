from django.db import models


# Models for the Hero Section
class HeroSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    button_text_primary = models.CharField(max_length=50)
    button_text_secondary = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HeroImage(models.Model):
    image = models.ImageField(upload_to='hero_images/')
    hero_section = models.ForeignKey(HeroSection, related_name='images', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.hero_section.title}"


class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about_us_images/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class OfferSection(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='offer_section_images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    color = models.CharField(max_length=7)  # e.g., Hex color code like '#FF5733'
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class OurServices(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)  # e.g., "3 months"
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

