# Generated by Django 2.2.5 on 2019-12-31 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nanapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qrcode',
            options={'ordering': ('created_at',), 'verbose_name': 'QrCode', 'verbose_name_plural': 'QrCodes'},
        ),
        migrations.AddField(
            model_name='presence',
            name='jour',
            field=models.DateField(null=True),
        ),
    ]
