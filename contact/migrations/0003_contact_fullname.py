# Generated by Django 4.0.2 on 2022-02-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_interest'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='fullname',
            field=models.CharField(blank=True, max_length=50, verbose_name='Full Name'),
        ),
    ]
