# Generated by Django 3.2.9 on 2021-11-21 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0002_photo_createat'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photoshare.customer'),
        ),
    ]
