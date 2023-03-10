# Generated by Django 4.1.3 on 2022-11-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigBazar_App', '0004_rename_image_categorydb_categoryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Quantity', models.CharField(blank=True, max_length=50, null=True)),
                ('Description', models.CharField(blank=True, max_length=50, null=True)),
                ('ProductImage', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('Category', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
