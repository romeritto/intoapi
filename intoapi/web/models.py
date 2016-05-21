from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Event(models.Model):
  name = models.CharField(max_length=200)
  organizer = models.ForeignKey(User)
  location = models.CharField(max_length=100, blank=True)
  description = models.TextField(default='', blank=True)
  STATUS_CHOICES = (
      ('OP', 'Open'),
      ('CL', 'Closed'),
      ('IO', 'Invite Only'),
      ('IN', 'Invisible'),
    )
  status =  models.CharField(max_length=2, choices=STATUS_CHOICES, default='IN')
  start_time = models.DateTimeField(default=timezone.now)
  end_time =  models.DateTimeField()
  facebook_share_img_url = models.URLField(default='', blank=True)
  ticketshop_url = models.URLField(default='', blank=True)
  sold_out = models.BooleanField(default=False)

  def __str__(self):
    return self.name

class EventProduct(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=6, decimal_places=2)

  def __str__(self):
    return self.name

class Guest(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  user = models.ForeignKey(User)

  def __str__(self):
    return self.user.username

class Product(models.Model):
  guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
  event_product = models.ForeignKey(EventProduct, on_delete=models.CASCADE)
  STATUS_CHOICES = (
      ('PE', 'Pending'),
      ('RE', 'Reserved'),
      ('TO', 'Timed out'),
      ('PP', 'Prending payment'),
      ('CA', 'Cancelled'),
      ('VA', 'Valid'),
      ('US', 'Used'),
      ('RV', 'Revoked'),
    )
  status =  models.CharField(max_length=2, choices=STATUS_CHOICES, default='PE')
  first_use_time = models.DateTimeField(null=True, blank=True)
  barcode = models.CharField(max_length=50, null=True, blank=True)

  def __str__(self):
    return self.event_product.name + ' - ' + self.status


