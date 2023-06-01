from django import forms
from .models import ContactForm, TrackingNumber
import uuid

class FeedBack(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'phone', 'message', 'subject']


