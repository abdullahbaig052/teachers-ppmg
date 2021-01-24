# Generated by Django 3.1.5 on 2021-01-24 15:38

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeachersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('profile_picture', models.CharField(max_length=256, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Provide phone number in international format', max_length=128, region=None)),
                ('room_number', models.CharField(max_length=4, null=True)),
                ('subjects_taught', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
