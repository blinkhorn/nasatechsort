from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import PrimaryTech

class PrimaryTechList(ListView):
    model = PrimaryTech

class PrimaryTechView(DetailView):
    model = PrimaryTech

class PrimaryTechCreate(CreateView):
    model = PrimaryTech
    fields = ['primary_tech_area']
    success_url = reverse_lazy('primary_tech_list')

class PrimaryTechUpdate(UpdateView):
    model = PrimaryTech
    fields = ['primary_tech_area']
    success_url = reverse_lazy('primary_tech_list')

class PrimaryTechDelete(DeleteView):
    model = PrimaryTech
    success_url = reverse_lazy('primary_tech_list')

# def index(request):
#     latest_choice = PrimaryTech.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('techsort/index.html')
#     context = {
#         'latest_choice': latest_choice,
#     }
#     return HttpResponse(template.render(context, request))
