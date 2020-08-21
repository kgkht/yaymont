# Generated by Django 3.1 on 2020-08-17 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_type', models.CharField(choices=[('S', 'Simple'), ('E', 'Egg')], default='S', help_text='Simple or Egg ?', max_length=1)),
                ('p_count', models.PositiveSmallIntegerField(default=1, help_text='How Many ?')),
                ('name', models.CharField(help_text='Enter Your Name', max_length=120)),
                ('phone', models.CharField(help_text='Enter Phone Number', max_length=13)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
