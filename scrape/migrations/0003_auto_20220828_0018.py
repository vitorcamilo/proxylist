# Generated by Django 3.2.5 on 2022-08-28 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0002_alter_editedfield_iplist_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iplist',
            name='anonymity',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='iplist',
            name='port',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='iplist',
            name='uptime',
            field=models.CharField(max_length=6),
        ),
    ]
