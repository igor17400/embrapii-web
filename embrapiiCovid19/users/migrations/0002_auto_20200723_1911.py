# Generated by Django 3.0.3 on 2020-07-23 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testtype',
            name='choice_to_exam',
        ),
        migrations.AddField(
            model_name='testtype',
            name='name',
            field=models.CharField(default='RT-PCR', max_length=50),
        ),
    ]
