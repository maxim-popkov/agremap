from django import forms
from agreapp.models import OrganizationRequest, Organization, Metropoliten


class OrganizationSearchForm(forms.Form):
    search_name = forms.CharField(max_length=128)
    search_city = forms.CharField(max_length=64)


class OrganizationRequestForm(forms.ModelForm):

    class Meta:
        model = OrganizationRequest
        exclude = ['is_deleted', 'is_approved']

# now dont used
class OrganizationForm(forms.ModelForm):

    metropoliten = forms.CharField(max_length=32, required=False)
    # metropolitens = forms.ModelMultipleChoiceField(queryset=Metropoliten.objects.all())

    class Meta:
        model = Organization
        exclude = ['metropolitens','longitude', 'latitude', 'srid', 'is_deleted', 'is_approved', 'num_views']

    def save(self, commit=True, force_insert=False, force_update=False, *args, **kwargs):
        org = super(OrganizationForm, self).save(commit=False, *args, **kwargs)
        if commit:
            org.save()
            if self.cleaned_data['metropoliten']:
                st = Metropoliten(city=self.cleaned_data['city'], 
                              station=self.cleaned_data['metropoliten'])
                st.save()
                org.metropolitens.add(st)
            org.save()
        return org
