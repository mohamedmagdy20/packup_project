# Generated by Django 4.0.3 on 2022-06-09 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_remove_ticket_doc_remove_ticket_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='BirthDay',
            field=models.DateField(),
        ),
    ]
