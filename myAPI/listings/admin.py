from django.contrib import admin
from listings.models import Band


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'shirt_size') # fields to display on Band list

admin.site.register(Band, BandAdmin) # Add Band model to admin site