from django.db import models

class SiteConfig(models.Model):
    site_title = models.CharField(max_length=200, default="CartWave")

    
    
