# Generated by Django 3.1.6 on 2021-07-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210706_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hierarchymodel',
            name='parent',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
