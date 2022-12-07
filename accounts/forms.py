from django import forms

from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
    
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Passwords does not match!'
            )
 
    #  USING BOOTSTARAP BUT THIS PRODUCING THIS FIELD REQURED
    # def __init__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, kwargs)
    #     self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
    #     self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
    #     self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
    #     self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
    #     self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'
    #     self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'