from django.forms import ModelForm
from .models import Messages
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.ModelForm):

    class Meta:
        model = Messages
        fields = ['Name', 'Location', 'PhoneNumber', 'Email', 'Message']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control' }),
            'Email': forms.TextInput(attrs={'class': 'form-control '}),
            'PhoneNumber': forms.TextInput(attrs={'class': 'form-control ','minlength': 10, 'maxlength': 15, 'required': True, 'type': 'number',}),
            'Location': forms.TextInput(attrs={'class': 'form-control'}),
            'Message': forms.Textarea(attrs={'class': 'form-control ','rows':4, 'cols':15,'placeholder':'Ge mer information om rengöringsprojektet här för att ge dig kvalificerade citat.'}),

        }
        error_messages = {
        'PhoneNumber': {
            'invalid': 'Please enter a valid phone number',
        },
        'Email': {
            'invalid': 'Your email address is incorrect',
        },

        }
        labels = {
            'Name': _('Namn'),
            'Location': _('Ort'),
            'PhoneNumber': _('Telefon'),
            'Email': _('E-postadress'),
            'Message': _('Meddelande')
        }


