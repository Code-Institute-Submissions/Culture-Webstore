# Generated by Django 3.1.4 on 2021-01-10 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20210110_1951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Enquiry', 'verbose_name_plural': 'Messages'},
        ),
    ]