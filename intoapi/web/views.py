from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Event, EventProduct, Guest, Product

# Create your views here.

def get_event_or_404(user, event_id):
  event = get_object_or_404(Event, pk=event_id)

  #if event wasn't created by logged user, act as if it DNE
  if (event.organizer != user):
    raise Http404("Event does not exist")
  else:
    return event

#VIEWS

@login_required
def index(request):
  return redirect('events')

@login_required
def events(request):
  event_list = Event.objects.filter(organizer=request.user, ).order_by('end_time')

  context = {
    'event_list' : event_list,
  }
  return render(request, 'web/events.html', context)

@login_required
def single_event(request, event_id):
  # also checks whether logged user made the event
  event = get_event_or_404(request.user, event_id)

  context = {
    'event' : event,
    'vars' : vars(event),
  }
  return render(request, 'web/single_event.html', context)

@login_required
def event_products(request, event_id):
  # also checks whether logged user made the event
  event = get_event_or_404(request.user, event_id)

  e_products = event.eventproduct_set.all()
  context = {
    'event' : event,
    'e_products' : e_products,
  }
  return render(request, 'web/event_products.html', context)

@login_required
def guests(request, event_id):
  # also checks whether logged user made the event
  event = get_event_or_404(request.user, event_id)
  guests = event.guest_set.all()
  context = {
    'event' : event,
    'guests' : guests,
  }
  return render(request, 'web/guests.html', context)

@login_required
def guest_products(request, event_id, guest_id):
  # also checks whether logged user made the event
  event = get_event_or_404(request.user, event_id)
  guest = get_object_or_404(Guest, pk=guest_id)
  guest.fullname = guest.user.first_name + ' ' + guest.user.last_name
  g_products = guest.product_set.all()
  context = {
    'event' : event,
    'guest' : guest,
    'g_products' : g_products,
  }
  return render(request, 'web/guest_products.html', context)