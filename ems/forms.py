from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm 

from django.forms import ModelForm
from ems.models import Booking

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        

class EditUserprofileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','date_joined','last_login']
        
class CreateBookForm(ModelForm):
    
    class Meta: 
        model=Booking
        fields='__all__'