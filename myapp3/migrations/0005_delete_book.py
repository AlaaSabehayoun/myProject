# Generated by Django 4.2.dev20221108194129 on 2024-04-01 21:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp3", "0004_employee_alter_book_id_alter_book_publication_date_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Book",
        ),
    ]
