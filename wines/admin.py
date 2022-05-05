from django.contrib import admin
from wines.models import WineModel, ColourModel




class WineModelAdmin(admin.ModelAdmin):
    list_display = ["name","strain",  "colour", "rating", "price"]
    ordering = ["name"]
    search_fields = ["name","strain",  "colour", "rating", "price"]
    list_filter = ("colour",)

    class Meta:
        model = WineModel



admin.site.register(WineModel, WineModelAdmin)
admin.site.register(ColourModel )