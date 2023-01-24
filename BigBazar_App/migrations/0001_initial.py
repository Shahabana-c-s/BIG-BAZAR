# Generated by Django 4.1.3 on 2022-11-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admindb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Image', models.ImageField(blank=True, max_length=50, null=True, upload_to='')),
                ('Username', models.CharField(blank=True, max_length=50, null=True)),
                ('Password', models.CharField(blank=True, max_length=50, null=True)),
                ('Confirm', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]