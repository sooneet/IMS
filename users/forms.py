from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'placeholder':'username',
                                }))
    password = forms.CharField(widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'placeholder':'password',
                                'type':'password',
                                 }))                                