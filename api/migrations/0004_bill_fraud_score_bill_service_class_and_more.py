# Generated by Django 4.0.5 on 2022-07-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_organization_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='fraud_score',
            field=models.FloatField(default=1, verbose_name='оценка мошенничества'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='service_class',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='service_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
