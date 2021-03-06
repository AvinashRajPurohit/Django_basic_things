# Generated by Django 3.0.8 on 2020-07-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=300)),
                ('phone_no', models.IntegerField()),
                ('email_id', models.EmailField(max_length=100)),
                ('dob', models.DateField(max_length=20)),
                ('pan_no', models.IntegerField()),
                ('pin_code', models.IntegerField()),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=100)),
                ('adhaar_img', models.ImageField(blank=True, null=True, upload_to='adhaar')),
                ('pan_img', models.ImageField(blank=True, null=True, upload_to='pan')),
            ],
        ),
    ]
