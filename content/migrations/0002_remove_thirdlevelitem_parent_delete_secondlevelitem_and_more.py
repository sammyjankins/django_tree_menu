# Generated by Django 4.1.7 on 2023-03-11 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thirdlevelitem',
            name='parent',
        ),
        migrations.DeleteModel(
            name='SecondLevelItem',
        ),
        migrations.DeleteModel(
            name='ThirdLevelItem',
        ),
    ]