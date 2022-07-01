from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FileUploadParser
from django_filters.rest_framework import DjangoFilterBackend

from .models import Client, Bill
from .serializers import (
    ClientListSerializer,
    BillCreateSerializer,
    OrganizationCreateSerializer,
    BillListSerializer
)


class OrganizationViewSet(ModelViewSet):
    http_method_names = ('post',)
    serializer_class = OrganizationCreateSerializer
    parser_class = (FileUploadParser,)


class BillViewSet(ModelViewSet):
    http_method_names = ('post',)
    serializer_class = BillCreateSerializer
    parser_class = (FileUploadParser,)


class ClientViewSet(ModelViewSet):
    http_method_names = ('get',)
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()


class BillViewSetList(ModelViewSet):
    http_method_names = ('get',)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['client', 'organization']
    serializer_class = BillListSerializer
    queryset = Bill.objects.all()
