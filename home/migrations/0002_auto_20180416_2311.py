# Generated by Django 2.0.3 on 2018-04-16 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='c_country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='college',
            name='c_locality',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='college',
            name='c_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='college',
            name='c_state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='d_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='home_state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='mail',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
