from django import forms
from .models import Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_name', 'vendor_license']
        
    #  USING BOOTSTARAP BUT THIS PRODUCING THIS FIELD REQURED
    # def __init__(self, *args, **kwargs):
    #     super(VendorForm, self).__init__(*args, kwargs)
    #     self.fields['vendor_name'].widget.attrs['placeholder'] = 'Enter Vendor Name'
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'