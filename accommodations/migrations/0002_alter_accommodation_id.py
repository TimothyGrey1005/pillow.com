# Generated by Django 5.0.1 on 2024-02-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
