from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from django_filters.rest_framework import DjangoFilterBackend


from .models import Client, Organization, Bill
from .serializers import (
    ClientListSerializer,
    BillCreateSerializer,
    OrganizationCreateSerializer,
    BillListSerializer
)


class OrganizationViewSet(ModelViewSet):
    http_method_names = ('post', )
    serializer_class = OrganizationCreateSerializer
    parser_class = (FileUploadParser,)


'''    def create(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        content_type = file.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        x = pd.read_excel(file, 'client')
        y = pd.read_excel(file, 'organization')
        json_str_x = x.to_json(force_ascii=False)
        json_str_y = y.to_json(force_ascii=False)
        print(json_str_y)
        print(json_str_x)
        return Response(response)'''


class BillViewSet(ModelViewSet):
    http_method_names = ('post', )
    serializer_class = BillCreateSerializer
    parser_class = (FileUploadParser,)


class ClientViewSet(ModelViewSet):
    http_method_names = ('get', )
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()


class BillViewSetList(ModelViewSet):
    http_method_names = ('get', )
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['client', 'organization']
    serializer_class = BillListSerializer
    queryset = Bill.objects.all()
