from django.db import models

from PIL import Image as PillowImage


class Image(models.Model):
    upload = models.ImageField(upload_to='images')

    # edit colors and save
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = PillowImage.open(self.upload.path)
        image = image.convert('1')
        image.save(self.upload.path)
