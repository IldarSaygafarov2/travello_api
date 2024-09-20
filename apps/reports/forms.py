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
            # 'marja',
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


# class AgentReportForm(forms.ModelForm):
#     class Meta:
#         model = models.AgentReport
#         fields = [
#             'date',
#             'agent_sum',
#             'direction',
#             'agent_payment',
#             'balance',
#             'comment',
#         ]
#         widgets = {
#             'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'agent_sum': forms.NumberInput(attrs={'class': 'form-control'}),
#             'direction': forms.TextInput(attrs={'class': 'form-control'}),
#             'agent_payment': forms.NumberInput(attrs={'class': 'form-control'}),
#             'balance': forms.NumberInput(attrs={'class': 'form-control'}),
#             'comment': forms.Textarea(attrs={'class': 'form-control'}),
#         }


# class SupplierReportForm(forms.ModelForm):
#     class Meta:
#         model = models.SupplierReport
#         fields = [
#             'date',
#             'agent_sum',
#             'direction',
#             'agent_payment',
#             'balance',
#             'comment',
#         ]
#         widgets = {
#             'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'agent_sum': forms.NumberInput(attrs={'class': 'form-control'}),
#             'direction': forms.TextInput(attrs={'class': 'form-control'}),
#             'agent_payment': forms.NumberInput(attrs={'class': 'form-control'}),
#             'balance': forms.NumberInput(attrs={'class': 'form-control'}),
#             'comment': forms.Textarea(attrs={'class': 'form-control'}),
#         }
