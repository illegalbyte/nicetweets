# Generated by Django 4.0 on 2022-01-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nicetweetsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='topic',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
