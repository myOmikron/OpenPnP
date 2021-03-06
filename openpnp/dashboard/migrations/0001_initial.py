# Generated by Django 3.0.6 on 2020-06-17 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('min_value', models.IntegerField(default=1)),
                ('max_value', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='TemplateSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('has_value', models.BooleanField(default=True)),
                ('min_value', models.IntegerField(default=1)),
                ('max_value', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('attributes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.TemplateAttribute')),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.TemplateSkill')),
            ],
        ),
    ]
