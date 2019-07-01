# Generated by Django 2.1.8 on 2019-06-24 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0027_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='origin',
            name='stock',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='origins', to='flydb.Fly'),
            preserve_default=False,
        ),
    ]