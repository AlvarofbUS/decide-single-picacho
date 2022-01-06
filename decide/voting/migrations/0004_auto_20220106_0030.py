# Generated by Django 2.0 on 2022-01-06 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='escanios',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='voting',
            name='postproc_mode',
            field=models.CharField(choices=[('IDENTITY', 'Identity'), ('DHONDT',"D'hondt"), ('SIMPLE', 'Simple')], default='IDENTITY', max_length=32),
        ),
    ]
