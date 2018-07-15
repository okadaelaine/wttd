from django.urls import path, register_converter

from eventex.lib.urlconverter import MaskConverter
from eventex.subscriptions.views import new, detail

register_converter(MaskConverter, 'mask')

app_name = 'subscriptions'

urlpatterns = [
    path('', new, name='new'),
    path('<mask:pk>/', detail, name='detail'),
]

