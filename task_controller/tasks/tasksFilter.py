import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')
    create_year = django_filters.NumberFilter(
        field_name='date_create',
        lookup_expr='year'
    )
    create_year__gt = django_filters.NumberFilter(
        field_name='date_create',
        lookup_expr='year__gt'
    )
    create_year__lt = django_filters.NumberFilter(
        field_name='date_create',
        lookup_expr='year__lt'
    )
    create_month = django_filters.NumberFilter(
        field_name='date_create',
        lookup_expr='month'
    )
    create_month__gt = django_filters.NumberFilter(
        field_name='date_create',
        lookup_expr='month__gt'
    )
    create_month__lt = django_filters.NumberFilter(
        field_name='date_create',
        lookup_expr='month__lt'
    )
    create_day = django_filters.NumberFilter(
        field_name='date_create',
        lookup_expr='day'
    )
    create_day__gt = django_filters.NumberFilter(
        field_name='date_create',
        lookup_expr='day__gt'
    )
    create_day__lt = django_filters.NumberFilter(
        field_name='date_create',
        lookup_expr='day__lt'
    )

    class Meta:
        model = Task
        fields = '__all__'
