from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from guestbook.models import Record


class RecordForm(forms.Form):
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('BLOCKED', 'Blocked'),
    )
    name = forms.CharField(max_length=100, required=True, label='Name')
    email = forms.EmailField(max_length=100, required=True, label='Email')
    text = forms.CharField(max_length=3000, required=True, label='Text', widget=widgets.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Status')

    class Meta:
        model = Record
        fields = ['name', 'email', 'text', 'created_at', 'updated_at', 'status']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError('Name must be longer than 2 symbols')
        return name

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 2:
            raise ValidationError('Text must be longer than 2 symbols')
        return text
