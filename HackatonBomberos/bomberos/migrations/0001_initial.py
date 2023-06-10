# Generated by Django 4.1.5 on 2023-06-10 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('idCargo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Cargo')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.AutoField(primary_key=True, serialize=False, verbose_name='Id comuna')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre comuna')),
            ],
        ),
        migrations.CreateModel(
            name='TipoEmergencia',
            fields=[
                ('idTipoEmergencia', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Tipo emergencia')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre emergencia')),
            ],
        ),
        migrations.CreateModel(
            name='Emergencia',
            fields=[
                ('idEmergencia', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Emergencia')),
                ('descripcion', models.CharField(max_length=500, verbose_name='Descripcion')),
                ('fechaInicio', models.DateField(verbose_name='Fecha inicio')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bomberos.tipoemergencia')),
            ],
        ),
        migrations.CreateModel(
            name='Cuartel',
            fields=[
                ('idCuartel', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('direccion', models.CharField(blank=True, max_length=20, null=True, verbose_name='Direccion')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bomberos.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('idCarro', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Carro')),
                ('patente', models.CharField(max_length=6, verbose_name='Patente')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('modelo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Modelo')),
                ('anno', models.IntegerField(verbose_name='Año')),
                ('capacidadPersonas', models.IntegerField(verbose_name='Capacidad personas')),
                ('capacidadLitros', models.IntegerField(verbose_name='Capacidad Litros')),
                ('cuartel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bomberos.cuartel')),
            ],
        ),
        migrations.CreateModel(
            name='Bombero',
            fields=[
                ('idBombero', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Bombero')),
                ('rut', models.IntegerField(verbose_name='Rut')),
                ('dv', models.CharField(max_length=1, verbose_name='Digito verificador')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apPaterno', models.CharField(max_length=50, verbose_name='Apellido paterno')),
                ('apMaterno', models.CharField(max_length=50, verbose_name='Apellido materno')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bomberos.cargo')),
            ],
        ),
    ]