from django import forms
from .models import Table


class SortForm(forms.Form):
    tables = Table.objects.all()
    ordering = forms.TypedChoiceField(label='Сортировать:', choices=[('name', 'По названию'),
                                                                     ('count', 'По количеству'),
                                                                     ('distance', 'По расстоянию')])


class ColumnForm(forms.Form):
    tables = Table.objects.all()
    column = forms.TypedChoiceField(label='Сортировать:', choices=[('name', 'По названию'),
                                                                   ('count', 'По количеству'),
                                                                   ('distance', 'По расстоянию')])


class ConditionForm(forms.Form):
    tables = Table.objects.all()
    condition = forms.TypedChoiceField(label='Условие:', choices=[('equals', 'Равно'),
                                                                  ('contains', 'Содержит'),
                                                                  ('over', 'Больше'),
                                                                  ('less', 'Меньше')])


class ValueForm(forms.Form):
    tables = Table.objects.all()
    value = forms.CharField(label='Значение:', widget=forms.TextInput)
