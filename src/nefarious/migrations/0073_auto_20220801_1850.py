# Generated by Django 3.0.2 on 2022-08-01 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0072_auto_20220714_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='QualityProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('profile', models.CharField(choices=[('any', 'any'), ('sd', 'sd'), ('hd-720p', 'hd-720p'), ('hd-720p-1080p', 'hd-720p-1080p'), ('hd-1080p', 'hd-1080p'), ('ultra-hd', 'ultra-hd')], max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='nefarioussettings',
            name='quality_profiles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nefarious.QualityProfile'),
        ),
    ]
