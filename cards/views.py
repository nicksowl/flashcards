from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Card

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by('box', '-date_create')
    

class CardCreateView(CreateView):
    model = Card
    fields = ['question', 'answer', 'box']
    success_url = reverse_lazy('card-create')
    # success_url = reverse_lazy('card-list')
    

class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy('card-list')
    