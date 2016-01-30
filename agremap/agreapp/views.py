from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404

from django.core.urlresolvers import reverse, reverse_lazy

from agreapp.forms import OrganizationForm

from agreapp.models import Organization
from agreapp.forms import OrganizationForm
from agreapp.mixins import AjaxableResponseMixin

# Create your views here.

def index(request):
    return render(request, 'agreapp/index.html')

def cities(request):
    return HttpResponse("Here you can all cities.")

def city(request, city_name):
    # city = city_name.title()
    # list_of_organizations = Organization.objects.filter(city=city_name)
    return HttpResponse("Here you can see all organizations in this city")


class OrganizationCreate(AjaxableResponseMixin, CreateView):
    form_class = OrganizationForm
    template_name = 'agreapp/add_clinic.html'
    success_url = reverse_lazy('agreapp:clinics_add')

    # def form_invalid(self, form):
    #     response = super(OrganizationCreate, self).form_invalid(form)
    #     if self.request.is_ajax():
    #         return JsonResponse(form.errors, status=400)
    #     else:
    #         return HttpResponseRedirect(reverse('agreapp:index'))


# def clinics_add(request):
#     output = ''
#     if request.method == 'POST':
#         form = OrganizationForm(request.POST)
#         if form.is_valid():
#             output += str(form)
#             output += 'success'
#             form.save()
#         else:
#             output += 'not success'
#             output += str(form.errors)

#     return HttpResponseRedirect(reverse('agreapp:index'))

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
