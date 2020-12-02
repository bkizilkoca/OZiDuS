# Generated by Django 3.1.4 on 2020-12-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZilData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dersbaslangicsaati', models.TimeField(default='09:00:00', verbose_name='Derslerin Başlangıç Saati')),
                ('toplanmasuresi', models.SmallIntegerField(default=600, verbose_name='Toplanma Süresi')),
                ('ogretmenzilsuresi', models.SmallIntegerField(default=180, verbose_name='Öğretmen Ders Bildirim Zili')),
                ('derssayisi', models.SmallIntegerField(default=10, verbose_name='Günlük Ders Sayısı')),
                ('derssuresi', models.SmallIntegerField(default=1800, verbose_name='Ders Süresi')),
                ('tenefussuresi', models.SmallIntegerField(default=600, verbose_name='Tenefüs Süresi')),
                ('oglenarasiders', models.SmallIntegerField(default=6, verbose_name='Öğlen Arası')),
                ('oglenarasisuresi', models.SmallIntegerField(default=2700, verbose_name='Öğlen Arası Süresi')),
                ('zilgun', models.SlugField(unique=True, verbose_name='Tanımlanan Gün')),
                ('active', models.BooleanField(default=False, verbose_name='Aktif Pasif')),
            ],
            options={
                'db_table': 'zildefault',
                'managed': True,
            },
        ),
    ]
