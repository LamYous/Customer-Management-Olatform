import django_filters
from django_filters import FilterSet, DateFilter
from .models import *

class OrderFilter(FilterSet):
    strat_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']