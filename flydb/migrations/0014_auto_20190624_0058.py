# Generated by Django 2.1.8 on 2019-06-23 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0013_auto_20190619_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
