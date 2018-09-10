from django.shortcuts import render
from django.views.generic import DetailView
from django_tables2 import RequestConfig
from .models import Person
from .tables import PersonTable


def persons(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'card_index/person_list.html', {'table': table})


class PersonDetailView(DetailView):
    model = Person
