from .models import Property
from .cache import Cache

def get_all_properties():
  cache = Cache()
  queryset = cache.get('all_properties')

  if queryset:
    return queryset
  
  queryset = Property.objects.all()
  cache.set('all_properties', queryset, 3600)
  return queryset
