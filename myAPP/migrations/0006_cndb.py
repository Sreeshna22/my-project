# Generated by Django 4.1.2 on 2023-01-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAPP', '0005_prodb'),
    ]

    operations = [
        migrations.CreateModel(
            name='cndb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Subject', models.CharField(blank=True, max_length=100, null=True)),
                ('Message', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
