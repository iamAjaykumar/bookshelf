from django.db import models
from django.db.models.base import Model
from PIL import Image,ImageOps
from django.contrib.auth.models import User

# Create your models here.
class BookInformation(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title=models.CharField(max_length=28)
    author=models.CharField(max_length=25)
    published_year=models.CharField(max_length=4)
    genre=models.CharField(max_length=10)
    picture=models.ImageField(upload_to='images')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img=Image.open(self.picture.path)
        try:

            img.ImageOps.exif_transpose(img)
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.picture.path)
        except:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.picture.path)



