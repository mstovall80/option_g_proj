# Generated by Django 2.2.4 on 2021-03-03 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('option_g_app', '0004_auto_20210302_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote', to='option_g_app.User'),
        ),
    ]
