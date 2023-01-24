# Generated by Django 4.1.3 on 2023-01-04 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigBazar_App', '0008_delete_logindb'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(blank=True, max_length=50, null=True)),
                ('Cemail', models.EmailField(blank=True, max_length=50, null=True)),
                ('Subject', models.CharField(blank=True, max_length=50, null=True)),
                ('Message', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='admindb',
            name='Email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]
