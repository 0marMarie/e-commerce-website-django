from django import forms

class Contact(forms.Form):

    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    message = forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Message','row':'5'}))