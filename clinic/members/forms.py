from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder': 'example@gmail.com'}))
    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
            super(RegisterUserForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({
                 'required' : '',
                 'name' :'username',
                 'id': 'username',
                 'type' :'text',
                 'class':'form-input',
                 'placeholder' :'username e.g Bright',
                 'maxlength' : '16',
                 'minlength' :'6'
            })
            self.fields['first_name'].widget.attrs.update({
                'required': '',
                'name': 'first_name',
                'id':' first_name',
                'type':'text',
                'class' : 'form-input',
                'placeholder' : 'firstname',
                'maxlength' :'16',
                'minlength' : ''
            })
            self.fields['last_name'].widget.attrs.update({
                 'required': '',
                'name': 'last_name',
                'id':' last_name',
                'type':'text',
                'class' : 'form-input',
                'placeholder' : 'last',
                'maxlength' :'16',
                'minlength' : ''
            })
            self.fields['email'].widget.attrs.update({
                 'required': '',
                'name': 'email',
                'id':' email',
                'type':'email',
                'class' : 'form-input',
                'placeholder' : 'Bright@gmail.com',
            })
            self.fields['password1'].widget.attrs.update({
                 'required': '',
                'name': 'password1',
                'id': 'password1',
                'type':'password',
                'class' : 'form-input',
                'placeholder' : 'paswword',
                'maxlength' :'22',
                'minlength' : '8'
            })
            self.fields['password2'].widget.attrs.update({
                 'required': '',
                'name': 'password2',
                'id': 'password2',
                'type':'password',
                'class' : 'form-input',
                'placeholder' : 'confirm password',
                'maxlength' :'22',
                'minlength' : '8'
            })
        
        
        
        


   
