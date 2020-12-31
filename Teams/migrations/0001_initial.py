# Generated by Django 3.0.4 on 2020-12-12 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('wins', models.IntegerField(blank=True, default=0, null=True)),
                ('losses', models.IntegerField(blank=True, default=0, null=True)),
                ('tie', models.IntegerField(blank=True, default=0, null=True)),
                ('score', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamScoring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wins', models.BooleanField()),
                ('losses', models.BooleanField()),
                ('tie', models.BooleanField()),
                ('Teams', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teams.Teams')),
            ],
        ),
    ]
