from email import message
from logging import PlaceHolder
from django import forms
from django.forms import ModelForm, TextInput
from .models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message_theme', 'message_text', 'phone', 'Email']
        widgets = {
            'message_text': forms.Textarea()
        }


    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form_element'})

        self.fields['message_text'].widget.attrs.update({'class':'form_element big_text_input'})

        self.fields['message_theme'].widget.attrs.update(placeholder='Тема')
        self.fields['message_text'].widget.attrs.update(placeholder='Текст сообщения')
        self.fields['phone'].widget.attrs.update(placeholder='Телефон')
        self.fields['Email'].widget.attrs.update(placeholder='Email')