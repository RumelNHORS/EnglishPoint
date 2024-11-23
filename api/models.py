from django.db import models


# Models for the Hero Section
class HeroSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    button_text_primary = models.CharField(max_length=50)
    button_text_secondary = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# Show the image on the hero section sliding
class HeroImage(models.Model):
    image = models.ImageField(upload_to='hero_images/')
    hero_section = models.ForeignKey(HeroSection, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for {self.hero_section.title}"

