# Generated by Django 3.1.1 on 2020-09-22 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
