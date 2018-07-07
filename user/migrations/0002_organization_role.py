# Generated by Django 2.0.5 on 2018-07-06 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='staff', max_length=120)),
                ('org_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Organization')),
                ('staff_id', models.ForeignKey(default='Anonymous', null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
        ),
    ]