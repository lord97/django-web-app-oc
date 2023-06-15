from django.contrib import admin

from listings.models import Band, Listing


class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre')

class ListingAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('title', 'sold', 'types','band')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing,ListingAdmin)