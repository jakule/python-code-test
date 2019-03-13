from django.contrib import admin

from shiptrader.models import Starship


class StarshipAdmin(admin.ModelAdmin):
    model = Starship


admin.site.register(Starship, StarshipAdmin)