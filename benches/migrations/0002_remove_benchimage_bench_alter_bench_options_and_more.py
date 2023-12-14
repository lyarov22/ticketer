# Generated by Django 4.2 on 2023-12-07 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('benches', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='benchimage',
            name='bench',
        ),
        migrations.AlterModelOptions(
            name='bench',
            options={'verbose_name': 'Мероприятие', 'verbose_name_plural': 'Мероприятие'},
        ),
        migrations.AlterModelOptions(
            name='benchdistrict',
            options={'ordering': ('name',), 'verbose_name': 'Местопроведения', 'verbose_name_plural': 'Местопроведения'},
        ),
        migrations.AlterModelOptions(
            name='benchtype',
            options={'ordering': ('name',), 'verbose_name': 'Тип', 'verbose_name_plural': 'Тип'},
        ),
        migrations.RemoveField(
            model_name='bench',
            name='author',
        ),
        migrations.RemoveField(
            model_name='bench',
            name='environment',
        ),
        migrations.RemoveField(
            model_name='bench',
            name='has_backrest',
        ),
        migrations.RemoveField(
            model_name='bench',
            name='has_bin',
        ),
        migrations.RemoveField(
            model_name='bench',
            name='location_latitude',
        ),
        migrations.RemoveField(
            model_name='bench',
            name='location_longitude',
        ),
        migrations.RemoveField(
            model_name='bench',
            name='rating',
        ),
        migrations.AddField(
            model_name='bench',
            name='name',
            field=models.CharField(db_index=True, default=1, max_length=200, verbose_name='Название мероприятия'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bench',
            name='avatar',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='bench_avatars/'),
        ),
        migrations.AlterField(
            model_name='bench',
            name='created_date',
            field=models.DateTimeField(verbose_name='Дата и время'),
        ),
        migrations.AlterField(
            model_name='bench',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='benches.benchdistrict'),
        ),
        migrations.AlterField(
            model_name='bench',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bench',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='benches.benchtype'),
        ),
        migrations.AlterField(
            model_name='benchdistrict',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Местопроведения'),
        ),
        migrations.AlterField(
            model_name='benchtype',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Тип'),
        ),
        migrations.DeleteModel(
            name='BenchEnvironment',
        ),
        migrations.DeleteModel(
            name='BenchImage',
        ),
    ]