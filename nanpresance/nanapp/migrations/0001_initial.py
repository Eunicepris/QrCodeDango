# Generated by Django 2.2.5 on 2020-01-11 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(choices=[('A', 'A'), ('B', 'B')], default='A', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Jour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Qrcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jours', models.CharField(editable=False, max_length=255, null=True)),
                ('debut_heure_arrivee', models.TimeField(default='08:00', null=True)),
                ('fin_heure_arrivee', models.TimeField(default='10:00', null=True)),
                ('titre_slug', models.SlugField(editable=False, max_length=255, null=True, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'QrCode',
                'verbose_name_plural': 'QrCodes',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacts', models.CharField(max_length=30, null=True)),
                ('genre', models.CharField(max_length=20, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('images', models.ImageField(default='photo.png', upload_to='images/avatar/')),
                ('specialite', models.CharField(max_length=255, null=True)),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('groupe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_groupe', to='nanapp.Groupe')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.AddField(
            model_name='groupe',
            name='jour_passage',
            field=models.ManyToManyField(related_name='jour', to='nanapp.Jour'),
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.CharField(editable=False, max_length=255, null=True)),
                ('heure_arrivee', models.TimeField(null=True)),
                ('heure_depart', models.TimeField(default='17:00', null=True)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('etudiant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userpresence', to='nanapp.Profile')),
                ('qrcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joursap', to='nanapp.Qrcode')),
            ],
            options={
                'unique_together': {('etudiant', 'qrcode')},
            },
        ),
    ]
