# Generated by Django 4.2.5 on 2024-07-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_ref_code_kyc'),
    ]

    operations = [
        migrations.AddField(
            model_name='kyc',
            name='identity_image',
            field=models.ImageField(blank=True, null=True, upload_to='kyc'),
        ),
    ]
