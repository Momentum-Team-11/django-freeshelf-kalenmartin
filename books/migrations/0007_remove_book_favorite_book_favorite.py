# Generated by Django 4.0.3 on 2022-03-10 16:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_rename_categories_book_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='favorite',
        ),
        migrations.AddField(
            model_name='book',
            name='favorite',
            field=models.ManyToManyField(related_name='favorite_books', to=settings.AUTH_USER_MODEL),
        ),
    ]
