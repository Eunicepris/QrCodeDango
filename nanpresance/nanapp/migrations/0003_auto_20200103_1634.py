# Generated by Django 2.2.5 on 2020-01-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nanapp', '0002_auto_20191231_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='jours',
            field=models.CharField(editable=False, max_length=255, null=True),
        ),
    ]