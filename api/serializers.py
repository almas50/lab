import json
import pandas as pd
from datetime import datetime

from rest_framework import serializers

from .models import Client, Organization, Bill
from utilities import fraud_detector, service_classifier


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'num_organizations', 'sum_bills')


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name',)


class OrganizationCreateSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False, required=True)

    class Meta:
        fields = ('file',)

    def create(self, validated_data):
        file = validated_data.get('file')
        clients = pd.read_excel(file, 'client')
        organizations = pd.read_excel(file, 'organization')
        clients_json = json.loads(clients.to_json(force_ascii=False))
        organizations_json = json.loads(organizations.to_json(force_ascii=False))
        for i in range(len(clients_json.get('name'))):
            Client.objects.update_or_create(name=clients_json.get('name').get(str(i)))
        for i in range(len(organizations_json.get('client_name'))):
            client = Client.objects.get(name=organizations_json.get('client_name').get(str(i)))
            address = organizations_json.get('address').get(str(i))
            name = organizations_json.get('name').get(str(i))
            if address:
                address = 'Адрес: ' + address
            Organization.objects.update_or_create(client=client, name=name, defaults={'address': address})
        return validated_data


class BillCreateSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False, required=True)

    class Meta:
        fields = ('file',)

    def create(self, validated_data):
        file = validated_data.get('file')
        bills = pd.read_excel(file)
        bills_json = json.loads(bills.to_json(force_ascii=False, date_format='iso'))
        for i in range(len(bills_json.get('client_name'))):
            client = Client.objects.get(name=bills_json.get('client_name').get(str(i)))
            organization = Organization.objects.get(name=bills_json.get('client_org').get(str(i)))
            date = datetime.strptime(bills_json.get('date').get(str(i))[:10], "%Y-%m-%d").date()
            service = bills_json.get('service').get(str(i))
            fraud_score = fraud_detector.fraud_detector(service)
            service_dict = service_classifier.service_classifier(service)
            service_class = list(service_dict.keys())[0]
            service_name = service_dict.get(service_class)
            num = bills_json.get('№').get(str(i))
            price = bills_json.get('sum').get(str(i))
            Bill.objects.update_or_create(num=num, organization=organization, defaults={'client': client, 'date': date,
                                                                                        'fraud_score': fraud_score,
                                                                                        'service_class': service_class,
                                                                                        'service_name': service_name,
                                                                                        'price': price,
                                                                                        'service': service})
        return validated_data


class BillListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('num', 'organization', 'client', 'price', 'date', 'service', 'service_class', 'service_name',
                  'fraud_score')
