from django.contrib import admin
from listings.models import Band, Listing


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'shirt_size') # fields to display on Band list

class ListingAdmin(admin.ModelAdmin):
    list_display = ('name', 'band') # fields to display on Band list


admin.site.register(Band, BandAdmin) # Add Band model to admin site
admin.site.register(Listing, ListingAdmin) # Add Band model to admin site