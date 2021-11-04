# Generated by Django 3.2.9 on 2021-11-04 08:03

import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=144)),
                ('description', models.TextField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('project_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('repo_link', models.URLField(max_length=300)),
                ('live_link', models.URLField(max_length=300)),
                ('technologies_used', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_wise', models.IntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('content_wise_average', models.FloatField(blank=True, default=0.0)),
                ('usability_wise', models.IntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('usability_wise_average', models.FloatField(blank=True, default=0.0)),
                ('design_wise', models.IntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('design_wise_average', models.FloatField(blank=True, default=0.0)),
                ('aggregate_average_rate', models.FloatField(blank=True, default=0.0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awwards_app.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('bio', models.TextField()),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]