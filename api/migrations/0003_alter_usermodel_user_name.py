# Generated by Django 4.0 on 2021-12-28 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_usermodel_first_name_alter_usermodel_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_name',
            field=models.CharField(default='', max_length=75),
            preserve_default=False,
        ),
    ]
