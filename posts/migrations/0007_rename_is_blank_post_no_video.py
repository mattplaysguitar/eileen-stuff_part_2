# Generated by Django 4.1.7 on 2023-03-16 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0006_post_is_blank"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="is_blank",
            new_name="no_video",
        ),
    ]
