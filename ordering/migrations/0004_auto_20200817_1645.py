# Generated by Django 3.1 on 2020-08-17 10:15

from django.db import migrations
import ordering.models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0003_auto_20200817_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordering',
            name='p_count',
            field=ordering.models.IntegerRangeField(help_text='How Many ?', verbose_name='Count'),
        ),
    ]
