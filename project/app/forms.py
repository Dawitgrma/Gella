from django.forms import ModelForm
from app.models import *

class pictureform(ModelForm):
    class Meta:
        model = picture
        fields = ('name','image','kind')