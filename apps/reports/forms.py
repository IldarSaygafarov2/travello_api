from django import forms
from apps.users.models import User
from django.contrib.auth.forms import AuthenticationForm
from . import models


class StaffAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class DailySalesForm(forms.ModelForm):
    class Meta:
        model = models.DailySales
        fields = [
            'date',
            'agent',
            'supplier',
            'agent_sum',
            'supplier_sum',
            'direction',
            'comment',
        ]
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'agent': forms.Select(attrs={'class': 'form-select'}),
            'supplier': forms.Select(attrs={'class': 'form-select'}),
            'agent_sum': forms.NumberInput(attrs={'class': 'form-control'}),
            'supplier_sum': forms.NumberInput(attrs={'class': 'form-control'}),
            'direction': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }


class DailySaleItemForm(forms.ModelForm):
    class Meta:
        model = models.DailySaleItem
        fields = [
            'date',
            'passenger',
            'direction',
            'agent',
            'agent_sum',
            'supplier',
            'supplier_sum',
            'comment'
        ]

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'passenger': forms.TextInput(attrs={'class': 'form-control'}),
            'direction': forms.TextInput(attrs={'class': 'form-control'}),
            'agent': forms.Select(attrs={'class': 'form-select'}),
            'agent_sum': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'supplier': forms.Select(attrs={'class': 'form-select'}),
            'supplier_sum': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
        }
