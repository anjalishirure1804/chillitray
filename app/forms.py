from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, PasswordChangeForm,PasswordResetForm,SetPasswordForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _


class CustomerRegistrationForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}
        
    def clean(self):
        cleaned_data = super(CustomerRegistrationForm, self).clean()
        username = cleaned_data.get('username')
        if username[0]!='a' or username[0]!='A':
            self.add_error('username', 'Username  Should  Start  with a/A')
        elif username[-1]!="0" or username[-1]!="1":
            self.add_error('username', 'Username Should End With 0/1')


        return cleaned_data



class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofoucs':True,'class':'form-control'}))
    password=forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-passsword','class':'form-control'}))