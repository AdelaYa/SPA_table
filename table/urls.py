from django.urls import path
from . import views
from .views import TableApiView

urlpatterns = [
    path('', views.table_list, name='index'),
    path('api/', TableApiView.as_view()),
]
