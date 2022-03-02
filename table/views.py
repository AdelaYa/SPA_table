from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Table
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import TableSerializer
from .forms import SortForm, ColumnForm, ConditionForm, ValueForm



def table_list(request):
    tables = Table.objects.all()

    form = SortForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['ordering']:
            tables = tables.order_by(form.cleaned_data['ordering'])
            for table in tables:
                if form == "name":
                    tables = tables.order_by("name")
                elif form == "count":
                    tables = tables.order_by("count")
                elif form == "distance":
                    tables = tables.order_by("distance")

    page = request.GET.get('page')
    paginator = Paginator(tables, 5)
    try:
        tables = paginator.page(page)
    except PageNotAnInteger:
        tables = paginator.page(1)
    except EmptyPage:
        tables = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'page': page,'tables': tables, })


class TableApiView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
