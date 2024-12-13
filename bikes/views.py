from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from bikes.forms import CykloModelForm
from bikes.models import *

def index(request):
    """Metoda připravuje pohled pro domovskou stránku - šablona index.html"""

    num_cyklos = Cyklo.objects.all().count()
    cyklos = Cyklo.objects.order_by('-rate')[:3]

    """ Do proměnné context, která je typu slovník (dictionary) uložíme hodnoty obou proměnných """
    context = {
        'num_cyklos': num_cyklos,
        'cyklos': cyklos
    }

    """ Pomocí metody render vyrendrujeme šablonu index.html a předáme ji hodnoty v proměnné context k zobrazení """
    return render(request, 'index.html', context=context)


class CykloListView(ListView):
    model = Cyklo

    context_object_name = 'cyklo_list'
    template_name = 'cyklo/list.html'
    paginate_by = 4

    def get_queryset(self):
        if 'type_bike_type' in self.kwargs:
            return Cyklo.objects.filter(type__bike_type=self.kwargs['type_bike_type']).all() # Get 5 books containing the title war
        else:
            return Cyklo.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['num_cyklos'] = len(self.get_queryset())
        if 'type_bike_type' in self.kwargs:
            context['view_title'] = f"Typ: {self.kwargs['type_bike_type']}"
            context['view_head'] = f"typ kola: {self.kwargs['type_bike_type']}"
        else:
            context['view_title'] = 'kola'
            context['view_head'] = 'Přehled kol'
        return context


class CykloDetailView(DetailView):
    model = Cyklo

    context_object_name = 'cyklo_detail'
    template_name = 'cyklo/detail.html'


def topten(request):
    return render(request, 'topten.html')


class CykloCreateView(CreateView):
    model = Cyklo
    fields = ['name', 'type', 'picture', 'description', 'release_date', 'rate']

class CykloUpdateView(UpdateView):
    model = Cyklo
    template_name = 'bikes/cyklo_bootstrap_form.html'
    form_class = CykloModelForm


class CykloDeleteView(DeleteView):
    model = Cyklo
    success_url = reverse_lazy('cyklo_list')

def prodejny(request):
    return render(request, 'prodejny.html')