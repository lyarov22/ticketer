# Generated by Django 4.2 on 2023-12-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benches', '0002_remove_benchimage_bench_alter_bench_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bench',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=10),
            preserve_default=False,
        ),
    ]