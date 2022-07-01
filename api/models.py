from django.db import models


class Client(models.Model):
    name = models.CharField(verbose_name='имя', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Клиент',
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name

    def __get_num_organizations(self):
        return self.organization_set.count()

    def __get_sum_bills(self):
        bills = Bill.objects.filter(client=self)
        sum = 0
        for bill in bills:
            sum += bill.price
        return sum

    num_organizations = property(__get_num_organizations)
    sum_bills = property(__get_sum_bills)


class Organization(models.Model):
    name = models.CharField(verbose_name='название компании', max_length=255)
    client = models.ForeignKey(Client, verbose_name='клиент компании', on_delete=models.CASCADE)
    address = models.CharField(verbose_name='адрес', max_length=255)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        unique_together = ['name', 'client']

    def __str__(self):
        return self.name

    def __get_fraud_weight(self):
        bills = Bill.objects.filter(client=self)
        count = 0
        for bill in bills:
            if bill.fraud_score >= 0.9:
                count += 1
        return count

    fraud_weight = property(__get_fraud_weight)


class Bill(models.Model):
    num = models.IntegerField(verbose_name='номер счета')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2)
    date = models.DateField(verbose_name='дата счета')
    service = models.CharField(verbose_name='название услуги', max_length=255)
    fraud_score = models.FloatField(verbose_name='оценка мошенничества')
    service_class = models.IntegerField()
    service_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        unique_together = ['organization', 'num']

    def __str__(self):
        return f'{self.num} {self.organization.name}'

