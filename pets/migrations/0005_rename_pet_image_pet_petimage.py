# Generated by Django 4.0.2 on 2022-02-11 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_pet_pet_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='pet_image',
            new_name='petImage',
        ),
    ]
