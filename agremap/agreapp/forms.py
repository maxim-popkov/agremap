from django import forms

class OrganizationForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(max_length=2048, required=False)
    
    city = forms.CharField(max_length=64)
    address = forms.CharField(max_length=256)
    metropoliten = forms.CharField(max_length=32, required=False)
    
    email = forms.EmailField(required=True)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                                    error_message = ("Phone number format: '+999999999'."),
                                    required=False)

    website = forms.URLField(max_length=64, required=False)
    