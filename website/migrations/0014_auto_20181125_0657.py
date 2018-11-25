# Generated by Django 2.1.2 on 2018-11-25 05:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20181125_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medication',
            name='form',
            field=models.CharField(choices=[('TB', 'tabletki'), ('ZS', 'zastrzyki'), ('KR', 'krople'), ('KP', 'kapsulki'), ('AM', 'ampulki'), ('FL', 'fiolki')], max_length=2),
        ),
    ]