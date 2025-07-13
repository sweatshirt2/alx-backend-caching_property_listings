from django.views.decorators.cache import cache_page

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Property
from .serializers import PropertySerializer

# Create your views here.
@cache_page(60 * 15)
@api_view(["GET"])
def property_list(request):
  if request.method == 'GET':
    properties = Property.objects.all()
    properties_serializer = PropertySerializer(properties, many=True)

    return Response(properties_serializer.data)
