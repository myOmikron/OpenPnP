# Generated by Django 3.0.8 on 2020-07-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monster', '0007_auto_20200715_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='comment',
            field=models.CharField(default='', max_length=255),
        ),
    ]
