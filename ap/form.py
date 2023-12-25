from typing import Any
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import ser,Tavarlar
from django import forms
class userform(UserCreationForm):
    class Meta(UserCreationForm):
        model=ser
        fields=('username','email','manzil','password1','password2','rasmingiz')
        labels={
            'username':'ism',
            'email':'gmeilingiz',
        }
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        
            

        
class userformch(UserChangeForm):
    class Meta:
        model=ser
        fields=('username','email','manzil','rasmingiz')


