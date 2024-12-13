from django.contrib import admin

# Import všech modelů, které obsahuje models.py
from django.db.models import Count
from django.utils.html import format_html

from .models import *

# Registrace modelů v administraci aplikace
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("bike_type", "cyklo_count")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _cyklo_count=Count("cyklo", distinct=True),
        )
        return queryset

    def cyklo_count(self, obj):
        return obj._cyklo_count

    cyklo_count.admin_order_field = "_cyklo_count"
    cyklo_count.short_description = "Počet cykloů"


@admin.register(Cyklo)
class CykloAdmin(admin.ModelAdmin):
    list_display = ("name", "release_year", "rate_percent",)

    def release_year(self, obj):
        return obj.release_date.year

    def rate_percent(self, obj):
        return format_html("<b>{} %</b>", int(obj.rate * 10))


    rate_percent.short_description = "Hodnocení cyklou"
    release_year.short_description = "Rok uvedení"

