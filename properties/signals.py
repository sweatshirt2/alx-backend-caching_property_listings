from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Property
from .cache import Cache

@receiver([post_save, Property])
def property_created(sender, instance, created, **kwargs):
  if created:
    cache = Cache()
    cache.delete("all_properties")

@receiver([post_delete, Property])
def property_deleted(sender, instance, **kwargs):
  cache = Cache()
  cache.delete("all_properties")
