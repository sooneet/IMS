from django import forms


class SupplierForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'name',
        'data-val':'true',
        'data-val-required':'please enter name',
        }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'address',
        'data-val':'true',
        'data-val-required':'please enter address',
        }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'username',
        'data-val':'true',
        'data-val-required':'please enter username',
        }))        
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'id':'email',
        'data-val':'true',
        'data-val-required':'please enter email',
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'id':'password',
        'data-val':'true',
        'data-val-required':'please enter password',
        }))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'id':'retype_password',
        'data-val':'true',
        'data-val-required':'please enter retype_password',
        }))                               

class BuyerForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'name',
        'data-val':'true',
        'data-val-required':'please enter name',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'id':'email',
        'data-val':'true',
        'data-val-required':'please enter email',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'address',
        'data-val':'true',
        'data-val-required':'please enter address',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'username',
        'data-val':'true',
        'data-val-required':'please enter username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'id':'password',
        'data-val':'true',
        'data-val-required':'please enter password',
    }))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'id':'retype_password',
        'data-val':'true',
        'data-val-required':'please enter retype_password',
    }))

