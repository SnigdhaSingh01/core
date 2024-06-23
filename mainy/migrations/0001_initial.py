# Generated by Django 4.1.4 on 2024-04-08 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='votingschedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.TextField(choices=[('Main', 'Main'), ('CEIT', 'CEIT'), ('CTE', 'CTE'), ('CAS', 'CAS'), ('COT', 'COT')], null=True)),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('governor', models.CharField(blank=True, max_length=50, null=True)),
                ('vice_governor', models.CharField(blank=True, max_length=50, null=True)),
                ('secretary', models.CharField(blank=True, max_length=50, null=True)),
                ('treasurer', models.CharField(blank=True, max_length=50, null=True)),
                ('auditor', models.CharField(blank=True, max_length=50, null=True)),
                ('pio', models.CharField(blank=True, max_length=50, null=True)),
                ('businessmanager', models.CharField(blank=True, max_length=50, null=True)),
                ('peaceofficer', models.CharField(blank=True, max_length=50, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MAINSSG_Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modal_id', models.CharField(default=main.models.modalID_generator, editable=False, max_length=50)),
                ('fullname', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='candidates')),
                ('bio', models.TextField(null=True)),
                ('position', models.TextField(choices=[('Governor', 'Governor'), ('Vice Governor', 'Vice Governor'), ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer'), ('Auditor', 'Auditor'), ('PIO', 'PIO'), ('Business Manager', 'Business Manager'), ('Peace Officer', 'Peace Officer')], null=True)),
                ('voters', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CTE_Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modal_id', models.CharField(default=main.models.modalID_generator, editable=False, max_length=50)),
                ('fullname', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='candidates')),
                ('bio', models.TextField(null=True)),
                ('position', models.TextField(choices=[('Governor', 'Governor'), ('Vice Governor', 'Vice Governor'), ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer'), ('Auditor', 'Auditor'), ('PIO', 'PIO'), ('Business Manager', 'Business Manager'), ('Peace Officer', 'Peace Officer')], null=True)),
                ('voters', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='COT_Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modal_id', models.CharField(default=main.models.modalID_generator, editable=False, max_length=50)),
                ('fullname', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='candidates')),
                ('bio', models.TextField(null=True)),
                ('position', models.TextField(choices=[('Governor', 'Governor'), ('Vice Governor', 'Vice Governor'), ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer'), ('Auditor', 'Auditor'), ('PIO', 'PIO'), ('Business Manager', 'Business Manager'), ('Peace Officer', 'Peace Officer')], null=True)),
                ('voters', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CEIT_Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modal_id', models.CharField(default=main.models.modalID_generator, editable=False, max_length=50)),
                ('fullname', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='candidates')),
                ('bio', models.TextField(null=True)),
                ('position', models.TextField(choices=[('Governor', 'Governor'), ('Vice Governor', 'Vice Governor'), ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer'), ('Auditor', 'Auditor'), ('PIO', 'PIO'), ('Business Manager', 'Business Manager'), ('Peace Officer', 'Peace Officer')], null=True)),
                ('voters', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CAS_Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modal_id', models.CharField(default=main.models.modalID_generator, editable=False, max_length=50)),
                ('fullname', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='candidates')),
                ('bio', models.TextField(null=True)),
                ('position', models.TextField(choices=[('Governor', 'Governor'), ('Vice Governor', 'Vice Governor'), ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer'), ('Auditor', 'Auditor'), ('PIO', 'PIO'), ('Business Manager', 'Business Manager'), ('Peace Officer', 'Peace Officer')], null=True)),
                ('voters', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
