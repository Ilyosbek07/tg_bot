# Generated by Django 4.0 on 2022-01-03 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_ordermodel_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='order',
            field=models.CharField(choices=[('TASDIQLANDI', 'Tasdiqlandi'), ('TASDIQLANMADI', 'tASDIQLANMADI')], default='TASDIQLANMADI', max_length=255),
        ),
    ]