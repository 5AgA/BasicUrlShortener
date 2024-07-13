from django.db import models

# Create your models here.
class URL(models.Model):
    num = models.AutoField(primary_key=True)
    origin_link = models.URLField(unique=True)

    def __str__(self):
        return f"{self.origin_link} -> {self.num}"