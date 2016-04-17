from django.db import models

# Create your models here.

class KeepInTouchEmail(models.Model):
    email = models.EmailField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email