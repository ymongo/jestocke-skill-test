# Register your models here.
from django.contrib import admin
from .models import StorageBox
from rangefilter.filters import NumericRangeFilterBuilder
from django.db.models import Q
import datetime

class StorageBoxAdmin(admin.ModelAdmin):
    list_display = ["id","created_at","get_owner_email","title","surface", "availability_start_date", "availability_end_date", "monthly_price"]
    list_filter = [("surface", NumericRangeFilterBuilder()),]
    ordering = ["-created_at"] 

    @admin.display(description='Owner Email Name', ordering='owner__email')
    def get_owner_email(self, obj):
        return obj.owner.email
    
    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request,
            queryset,
            search_term,
        )
        request.POST = request.POST.copy()

        try:
            availability_start = request.POST.get('availability-start', None)
            availability_end = request.POST.get('availability-end', None)
            if availability_start and availability_start != '':
                start = datetime.datetime.strptime(availability_start, '%Y-%m-%d')
                queryset = queryset.filter(Q(availability_start_date__gte=start) | 
                                           Q(availability_start_date__lte=start, availability_end_date__gte=start))
            if availability_end and availability_end != '':
                end = datetime.datetime.strptime(availability_end, '%Y-%m-%d')
                queryset = queryset.filter(Q(availability_end_date__lte=end) | 
                                           Q(availability_start_date__lte=end, availability_end_date__gte=end))
        except ValueError:
            pass
        return queryset, may_have_duplicates

admin.site.register(StorageBox, StorageBoxAdmin)    