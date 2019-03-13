from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from shiptrader.models import Starship, Listing
from shiptrader.serializers import StarshipSerializer, ListingSerializer


class StarshipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Starships to be viewed or edited.
    """
    queryset = Starship.objects.all().order_by('name')
    serializer_class = StarshipSerializer


class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Listings to be viewed or edited.
    """
    queryset = Listing.objects.all().order_by('-created')
    serializer_class = ListingSerializer
    filterset_fields = ('ship_type__starship_class', )
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('active', 'price')
