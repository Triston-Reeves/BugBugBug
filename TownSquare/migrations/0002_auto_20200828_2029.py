# Generated by Django 3.1 on 2020-08-28 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TownSquare', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='filed_by',
        ),
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('N', 'New'), ('P', 'In Progress'), ('D', 'Done'), ('I', 'Invalid')], default='N', max_length=1),
        ),
    ]
