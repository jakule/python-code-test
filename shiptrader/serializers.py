from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from shiptrader.models import Starship, Listing


class StarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starship
        fields = ('name', 'starship_class', 'manufacturer', 'length',
                  'hyperdrive_rating', 'cargo_capacity', 'crew', 'passengers')


class ListingSerializer(serializers.ModelSerializer):
    ship_name = serializers.CharField(max_length=255, write_only=True)
    ship_type = StarshipSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = ('id', 'price', 'ship_type', 'active', 'created', 'ship_name')

    def create(self, validated_data):
        ship_name = validated_data.pop('ship_name')
        ship = get_object_or_404(Starship, name=ship_name)
        return Listing.objects.create(**validated_data, ship_type=ship)
