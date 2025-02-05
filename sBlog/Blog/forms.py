from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User 
from . models import Post , Contact






class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets ={'username':forms.TextInput(attrs={'class':'form-control'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={  'autofocus':True,
     'class':'form-control'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'autocomplete':'current-password',
     'autofocus':True,'class':'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['tittle', 'desc']

        labels={'tittle':'TITTLE', 'desc':'DESC'}

        widgets={'tittle':forms.TextInput(attrs={'class':'form-control'}),
                  'desc':forms.Textarea(attrs={'class':'form-control'}),}
        


class ContactForm(forms.ModelForm):
    class Meta:
        model  = Contact
        fields = ['name', 'email', 'address','message']
        
