from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
)


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = forms.cleaned_data.get("username")
		password = forms.cleaned_data.get("password")
       
		
		if username and password:
			user = authenticate(username=username, password=password)
        	
			if not user:
				raise forms.ValidationError("This user does not exist")
        		

			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")
			if not user.is_active:
				raise forms.ValidationError("This user is not longer active")
		return super(UserLoginForm, self).clean(*args, **kwargs)
