# Generated by Django 5.0.2 on 2024-03-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='category_images/'),
        ),
    ]