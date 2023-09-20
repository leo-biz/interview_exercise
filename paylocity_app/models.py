from django.db import models
import uuid

class SecurityFeature(models.Model):
    class FeatureTypes(models.TextChoices):
        PLATFORM = 'Platform'
    feature_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    type = models.CharField(
        max_length=200, 
        choices=FeatureTypes.choices, 
        default=FeatureTypes.PLATFORM)
    
    description = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}: {self.description[:20]}'
