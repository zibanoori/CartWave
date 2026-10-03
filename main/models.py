from django.db import models

class SiteConfig(models.Model):
    site_title = models.CharField(max_length=200, default="CartWave")
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="site/logo/", blank=True, null=True)
    favicon = models.ImageField(upload_to="site/favicon/", blank=True, null=True)
    site_name = models.CharField(max_length=100, default="CartWave", verbose_name="Site Name")
    
    class Meta:
        verbose_name = "site configuration"
        verbose_name_plural = "site configurations"
        
    def __str__(self):
        return self.site_title