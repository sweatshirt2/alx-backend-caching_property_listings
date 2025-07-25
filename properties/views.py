from django.views.decorators.cache import cache_page
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Property
from .serializers import PropertySerializer
from .utils import get_all_properties

# Create your views here.
@cache_page(60 * 15)
@api_view(["GET"])
def property_list(request):
  if request.method == 'GET':
    properties = get_all_properties()
    properties_serializer = PropertySerializer(properties, many=True)

    return JsonResponse({"properties": properties_serializer.data}, safe=False)
