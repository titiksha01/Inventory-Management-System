from django import forms
from .models import Stock
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(max_length=150)
    dep_no = forms.IntegerField()

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2','dep_no' )



class StockCreateForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'item_name', 'quantity','created_by' ]