# Generated by Django 3.0.8 on 2020-07-15 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monster', '0004_auto_20200715_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='race',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='monster.Race'),
        ),
    ]