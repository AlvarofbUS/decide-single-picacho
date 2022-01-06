

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
    ]
