from django import forms

from .models import Vendor
from accounts.validators import allow_only_image_validator


class VendorForm(forms.ModelForm):
    vendor_license = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_image_validator])
    class Meta:
        model = Vendor
        fields = ['vendor_name', 'vendor_license']
        
    #  USING BOOTSTARAP BUT THIS PRODUCING THIS FIELD REQURED
    # def __init__(self, *args, **kwargs):
    #     super(VendorForm, self).__init__(*args, kwargs)
    #     self.fields['vendor_name'].widget.attrs['placeholder'] = 'Enter Vendor Name'
    #     for field in self.fields:
    #     self.fields[field].widget.attrs['class'] = 'form-control'