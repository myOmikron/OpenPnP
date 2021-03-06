# Generated by Django 3.0.8 on 2020-07-15 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monster', '0011_remove_sense_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavingThrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='monster',
            name='saving_throws',
            field=models.ManyToManyField(to='monster.SavingThrow'),
        ),
    ]
