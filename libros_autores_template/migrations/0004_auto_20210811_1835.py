# Generated by Django 3.2.5 on 2021-08-11 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros_autores_template', '0003_authors_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='books',
        ),
        migrations.AddField(
            model_name='authors',
            name='book',
            field=models.ManyToManyField(related_name='authors', to='libros_autores_template.books'),
        ),
    ]
