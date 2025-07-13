from django.core.cache import cache

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

def get_redis_cache_metrics():
  client = cache.client.get_client(write=True)
  info = client.info()

  keyspace_hits = info.get("keyspace_hits")
  keyspace_misses = info.get("keyspace_misses")
