# Generated by Django 3.2.16 on 2022-11-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0006_alter_data_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='link',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='slug',
        ),
        migrations.AddField(
            model_name='district',
            name='link',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
