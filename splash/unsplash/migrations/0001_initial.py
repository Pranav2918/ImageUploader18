# Generated by Django 3.1.7 on 2021-04-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='myimg')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
