from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class kind(models.Model):
    name = models.CharField(max_length=50)
    numbers = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return str(self.name)


class picture(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    likes = models.PositiveIntegerField(default=0)
    uploader = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    kind = models.ForeignKey(kind,default='',on_delete=models.SET_NULL,null=True)
    
    def delete(self):
        self.image.delete()
        super().delete()
        
    class Meta:
        ordering = ['-likes']
        
    
    def __str__(self):
        return self.name
        
class like(models.Model):
    picture = models.ForeignKey(picture,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    kind = models.ForeignKey(kind,default='',on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.picture.name
    