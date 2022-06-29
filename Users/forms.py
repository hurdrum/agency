from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'phone', 'email', 'photo']
        labels = {
            'name':'Имя',
            'surname':'Фамилия',
            'phone':'Телефон',
            'photo':' Изменить фото профиля'
        }
        widgets = {
            'photo': forms.FileInput()
        }

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form_element form_element_profile'})


class CustomUserCreationForm(SignupForm):
    class Meta:
        model = User


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        
        self.fields['password'].widget.attrs.update({'class':'form_element form_element_profile'})
        self.fields['login'].widget.attrs.update({'class':'form_element form_element_profile'})
        self.fields['remember'].widget.attrs.update({'class':'custom-checkbox'})


        self.fields['password'].label = 'Пароль'
        self.fields['login'].label = 'Email'
        self.fields['remember'].label = 'Запомнить меня'

        self.fields['password'].widget.attrs.update({'placeholder':'*******'})
        self.fields['login'].widget.attrs.update({'placeholder':'example@gmail.com'})

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):    
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form_element form_element_profile'})

        self.fields['email'].label = 'Введите Email'        
        self.fields['password1'].label = 'Придумайте пароль'
        self.fields['password2'].label = 'Повоторите пароль'

        self.fields['email'].widget.attrs.update({'placeholder':'example@gmail.com'})
        self.fields['password1'].widget.attrs.update({'placeholder':'*******'})
        self.fields['password2'].widget.attrs.update({'placeholder':'*******'})

class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):    
        super(CustomResetPasswordForm, self).__init__(*args, **kwargs)

        self.fields['email'].label = ''
        self.fields['email'].widget.attrs.update({'placeholder':'example@gmail.com'})
        self.fields['email'].widget.attrs.update({'class':'form_element form_element_profile'})