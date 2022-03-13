import profile
from django import forms
from .models import User
import sys
sys.path.append("..")
class Updateuserinfo(forms.ModelForm):    
    class Meta:
        model = User
        fields = ["username","profile_image"] 
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your new user name'}),
        }
        profile_image=forms.ImageField()  
        
