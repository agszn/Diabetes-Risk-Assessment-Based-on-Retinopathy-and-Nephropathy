# Generated by Django 5.0.3 on 2024-05-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0014_alter_consumer_id_alter_contact_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consumer",
            name="content",
            field=models.TextField(
                blank=True, null=True, verbose_name="Medicine Content"
            ),
        ),
        migrations.AlterField(
            model_name="consumer",
            name="email",
            field=models.EmailField(
                blank=True, max_length=277, null=True, verbose_name="Student Email"
            ),
        ),
        migrations.AlterField(
            model_name="consumer",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="consumer_images/",
                verbose_name="Medicine Image",
            ),
        ),
        migrations.AlterField(
            model_name="consumer",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Medicine Name"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="message",
            field=models.CharField(max_length=1000),
        ),
    ]