# Generated by Django 4.0.2 on 2022-02-11 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_rename_pet_image_pet_petimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='petImage',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name="Add pet's image.."),
        ),
    ]