from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django import forms

class SingupForm(UserCreationForm):
    first_name=forms.CharField(
        max_length=50,
         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your firstname'}))

    last_name=forms.CharField(
        max_length=50,
         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your lastname'}))
    
    email=forms.CharField(
        max_length=50,
         widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter your email'}))
    
    username=forms.CharField(
        max_length=50,
         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your username'}))
    
    password1=forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'from-control',
            'name':'password',
            'type':'password',
            'placeholder':'enter your password '
        })
    )

    password2=forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'from-control',
            'name':'password',
            'type':'password',
            'placeholder':'enter your password again '
        })
    )

    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')


class UpdateUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your firstname'}))

    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your lastname'}))

    email = forms.CharField(
        max_length=50,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter your email'}))

    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your username'}))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')



class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'from-control',
            'name': 'password',
            'type': 'password',
            'placeholder': 'enter your password '})),

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'from-control',
            'name': 'password',
            'type': 'password',
            'placeholder': 'enter your password again '}))

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')

















