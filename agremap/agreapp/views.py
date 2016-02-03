# Utils
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
# Views
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView
# Forms
from django.views.generic.edit import FormMixin
# App moduls
from agreapp.forms import OrganizationRequestForm, OrganizationForm, OrganizationSearchForm

from agreapp.models import Organization
from agreapp.mixins import AjaxableResponseMixin


def index(request):
    return render(request, 'agreapp/index.html')

def cities(request):
    return HttpResponse("Here you can all cities.")

def city(request, city_name):
    # city = city_name.title()
    # list_of_organizations = Organization.objects.filter(city=city_name)
    return HttpResponse("Here you can see all organizations in this city")


def services(request):
    return HttpResponse("All services.")

def chains(request):
    return HttpResponse("All dental chains.")

def add(request, city_name):
    # city = city_name.title()
    return HttpResponse("Here you can add new clinic for the")

def search(request, city_name):
    return render(request, 'agreapp/search_results.html')

def search_results(request, city_name):
    # city = city_name.title()
    # obj = Organization.objects.filter(city=city_name)
    return HttpResponse("This is a list of all organizations in the.")

def detail_view(request, city_name, organization_id):
    # city = city_name.title()
    # obj = Organization.objects.filter (pk=organization_id)
    return HttpResponse("detail view")


#==== Class Based Views ====
class IndexView():
    pass


class OrganizationSearchView(ListView):
    model = Organization
    template_name = 'agreapp/search_results.html'
    context_object_name="organization_list"
    form_class = OrganizationSearchForm

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        name = ''
        if form.is_valid():
            try:
                name = form.cleaned_data['search_name']
            except:
                name = ''
                
        organization_list = None
        if name != '':
            organization_list = self.model.objects.filter(name__icontains = name)
        else:
            organization_list = []
        return organization_list


class OrganizationCreateSuccess(TemplateView):
    template_name = 'agreapp/add_clinic_success.html'


class OrganizationCreate(AjaxableResponseMixin, CreateView):
    form_class = OrganizationRequestForm
    template_name = 'agreapp/add_clinic.html'
    success_url = reverse_lazy('agreapp:clinic_add_success')
