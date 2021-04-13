# Generated by Django 3.2 on 2021-04-12 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('febre', models.BooleanField(default=False)),
                ('tosse', models.BooleanField(default=False)),
                ('cansaco', models.BooleanField(default=False)),
                ('desconforto', models.BooleanField(default=False)),
                ('dor_garganta', models.BooleanField(default=False)),
                ('diarreia', models.BooleanField(default=False)),
                ('conjuntivite', models.BooleanField(default=False)),
                ('dor_cabeca', models.BooleanField(default=False)),
                ('perda_paladar', models.BooleanField(default=False)),
                ('erupcao_cutanea', models.BooleanField(default=False)),
                ('falta_ar', models.BooleanField(default=False)),
                ('dor_peito', models.BooleanField(default=False)),
                ('perda_fala', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
