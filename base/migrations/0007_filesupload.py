# Generated by Django 3.2.14 on 2022-08-31 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_emergency_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.FileField(upload_to='')),
                ('Catagery', models.CharField(max_length=100)),
                ('Topic', models.CharField(max_length=100)),
            ],
        ),
    ]
