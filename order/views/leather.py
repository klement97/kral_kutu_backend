from rest_framework.generics import ListAPIView

from order.models import Leather, LeatherSerial
from order.serializers.leather import LeatherSerialSerializer, LeatherSerializer


class LeatherListAPIView(ListAPIView):
    serializer_class = LeatherSerializer
    queryset = Leather.objects. \
        select_related('serial'). \
        filter(deleted=False)
    filterset_fields = ('code', 'serial')


class LeatherSerialListAPIView(ListAPIView):
    serializer_class = LeatherSerialSerializer
    queryset = LeatherSerial.objects.filter(deleted=False)