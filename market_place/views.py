from django.shortcuts import render
from .models import StorageBox
import django_tables2 as tables
from .models import StorageBox
from django_tables2 import SingleTableView, Table, Column
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_filters import FilterSet

class StorageBoxTable(Table):
    num_route_concat = Column(verbose_name= 'Address', order_by=("street_number"))
    
    class Meta:
        model = StorageBox
        template_name = "django_tables2/bootstrap.html"
        fields = ("storage_type", "title", "surface","description",
                  "monthly_price","num_route_concat",
                  "postal_code", "city", "availability_start_date", "availability_end_date")


class StorageBoxView(SingleTableView):
    model = StorageBox
    table_class = StorageBoxTable
    template_name = 'market_place/index.html'
    
class StorageBoxFilter(FilterSet):
    class Meta:
        model = StorageBox
        fields = {"surface": ["exact"],"monthly_price": ["exact"],"postal_code": ["exact"],"city": ["exact"], "availability_start_date": ["exact"], "availability_end_date": ["exact"]  }

class FilteredStorageBoxListView(SingleTableMixin, FilterView):
    table_class = StorageBoxTable
    model = StorageBox
    template_name = "market_place/index.html"

    filterset_class = StorageBoxFilter