# Generated by Django 4.1.3 on 2022-11-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigBazar_App', '0006_rename_description_productdb_product_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='logindb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LUsername', models.CharField(blank=True, max_length=50, null=True)),
                ('LPassword', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
