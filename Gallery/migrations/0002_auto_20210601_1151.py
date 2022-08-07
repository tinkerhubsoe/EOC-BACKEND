# Generated by Django 3.2.3 on 2021-06-01 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('UniqueID', models.AutoField(primary_key=True, serialize=False)),
                ('ProgramId', models.IntegerField()),
                ('Imgname', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='programs',
            name='ProgramImageCount',
        ),
    ]