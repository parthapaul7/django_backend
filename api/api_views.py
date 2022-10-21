from rest_framework.generics import ListAPIView 
from .seriazers import CountrySerializer
from .models import Country


class CountryList(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
