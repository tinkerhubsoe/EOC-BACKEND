# Generated by Django 3.2.3 on 2021-06-01 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0005_alter_postimage_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programs',
            name='image',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]