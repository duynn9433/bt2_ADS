import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegisteForm(forms.Form):
    username = forms.CharField(label='Account', max_length=30)
    email=forms.EmailField(label='Email')
    password1=forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhap lai', widget=forms.PasswordInput())

    #clean - kiem tra + field muon ktra
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            p1 = self.cleaned_data['password1']
            p2 = self.cleaned_data['password2']
            if p1==p2 and p1:
                return p2
        raise forms.ValidationError("Mat khau khong hop le")

    def clean_username(self):
        u = self.cleaned_data['username']
        if not re.search(r'^\w+$', u): #co ki tu dac bit
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=u)
        except ObjectDoesNotExist:
            return u
        return forms.ValidationError("Tài khoản đã tồn tại")

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],
                                 email=self.cleaned_data['email'],
                                 password=self.cleaned_data['password1'], )

