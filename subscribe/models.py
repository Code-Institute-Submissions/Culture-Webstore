from django.db import models

# Create your models here.
class Subscribers(models.Model):

    class Meta:
        verbose_name_plural = 'Subscribers'
        
    email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.email