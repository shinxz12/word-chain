# Generated by Django 5.0.6 on 2024-06-23 10:02

from django.db import migrations, models


def initial_data(apps, schema_editor):
    Word = apps.get_model("common", "Word")
    with open('common/resources/words.txt', 'r') as file:
        words = file.readlines()
        Word.objects.bulk_create([
            Word(word=word.strip()) for word in words
        ])

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Word",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("index", models.PositiveIntegerField(default=1)),
                ("word", models.CharField(max_length=100)),
                ("meaning", models.CharField(blank=True, max_length=255, null=True)),
                ("example", models.TextField(blank=True, null=True)),
            ],
            options={"abstract": False,},
        ),
        migrations.RunPython(initial_data),
    ]