# Generated by Django 3.0.6 on 2020-05-26 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_web', '0003_auto_20200525_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='ingredient',
            field=models.TextField(null=True),
        ),
    ]