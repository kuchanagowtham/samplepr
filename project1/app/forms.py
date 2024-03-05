from django import forms
from .models import Myregistration

class MyregistrationForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'pattern':'[a-zA-Z]+'}),required=True,max_length=100)
	username = forms.CharField(widget=forms.TextInput(attrs={'pattern':'[a-zA-Z]+'}),required=True,max_length=100)
	password = forms.CharField(widget=forms.TextInput(attrs={'pattern':'(?=\d)(?=.*[a-z])(?=.*[A-Z]).{8,}','title':'Must contain at least one uppercase and one lowercase and one number , and at least 8 or more characters '}),required=True,max_length=100)
	mobile = forms.CharField(widget=forms.TextInput(attrs={'pattern':'[6789][0-9]{9}'}),required=True,max_length=100)
	email = forms.CharField(widget=forms.TextInput(attrs={'pattern':'[a-z0-9._=-]+@[a-z0-9.-]+\.[a-z]{2,}'}),required=True,max_length=100)
	adress = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols': 22}), required=True,max_length=250)

	class Meta():
		model = Myregistration
		fields='__all__'
	