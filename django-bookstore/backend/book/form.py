from django.forms import ModelForm
from.models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']
        
    class createcustomerForm(ModelForm):
        class Meta:
            model=Customer
            fields='__all__'
            exclude=['user']