# Generated by Django 2.0.2 on 2018-07-07 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_organization_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(default='Staff', max_length=120),
        ),
    ]