# Generated by Django 3.0.4 on 2020-03-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200314_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='displayname',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
