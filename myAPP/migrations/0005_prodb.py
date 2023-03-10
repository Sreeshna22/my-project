# Generated by Django 4.1.2 on 2022-12-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAPP', '0004_regdb_delete_studentss'),
    ]

    operations = [
        migrations.CreateModel(
            name='prodb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Product_Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Product_Price', models.IntegerField(blank=True, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=30, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
    ]
