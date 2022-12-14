# Generated by Django 4.0.6 on 2022-08-09 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0002_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='properties',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='realestate.cards'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
