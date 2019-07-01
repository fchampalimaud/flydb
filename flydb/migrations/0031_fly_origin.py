# Generated by Django 2.1.8 on 2019-06-26 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0030_auto_20190626_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='fly',
            name='origin',
            field=models.CharField(choices=[('center', 'Stock Center'), ('internal', 'Internal Lab'), ('external', 'External Lab')], default='center', max_length=8),
        ),
    ]
