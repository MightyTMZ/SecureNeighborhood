# Generated by Django 4.2.7 on 2024-02-17 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_address_communitymember_communitymemberendorsement'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='house_number',
            field=models.CharField(default='-', max_length=50),
            preserve_default=False,
        ),
    ]