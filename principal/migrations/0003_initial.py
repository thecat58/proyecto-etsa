# Generated by Django 4.2 on 2023-04-26 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('principal', '0002_delete_agendamiento_delete_cateserv_delete_contrato_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamiento',
            fields=[
                ('hora', models.IntegerField(db_comment='guarda la hora de la cita \n', primary_key=True, serialize=False)),
                ('lugar', models.CharField(blank=True, db_comment='guarda la ubicacion de la cita ', max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, db_comment='guarda el nombre de quien cita ', max_length=45, null=True)),
            ],
            options={
                'db_table': 'agendamiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cateserv',
            fields=[
                ('idcateserv', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'cateserv',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('idcontrato', models.IntegerField(db_comment='guarda registro de contrato que realiza la empresa ', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, db_comment='guarda los terminos y condiciones de cada contrato ', max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, db_comment='guarda el nombre del contrato ', max_length=45, null=True)),
                ('servicio_idservicio', models.IntegerField()),
                ('persona_idpersona', models.IntegerField()),
            ],
            options={
                'db_table': 'contrato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ctaller',
            fields=[
                ('ctaller', models.IntegerField(db_comment='guarda el registro de cada taller ', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, db_comment='guarda el servicio que a prestar ', max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, db_comment='guarda el nombre de cada taller ', max_length=45, null=True)),
            ],
            options={
                'db_table': 'ctaller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cuerpo',
            fields=[
                ('idcuerpo', models.IntegerField(primary_key=True, serialize=False)),
                ('idcabeza', models.CharField(blank=True, max_length=45, null=True)),
                ('cantidad', models.CharField(blank=True, max_length=45, null=True)),
                ('valorunitariol', models.CharField(blank=True, max_length=45, null=True)),
                ('valortotal', models.CharField(blank=True, max_length=45, null=True)),
                ('factcabeza_idfactura', models.IntegerField()),
                ('scripcion_idscripcion', models.IntegerField()),
            ],
            options={
                'db_table': 'cuerpo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('iddepartamento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('codigo', models.CharField(blank=True, max_length=45, null=True)),
                ('municipio_idmunicipio', models.IntegerField()),
            ],
            options={
                'db_table': 'departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('idempresa', models.IntegerField(db_comment='guarda el numero de registro de la empresa', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_comment='guarda el nombre de la empresa ', max_length=45, null=True)),
                ('direccion', models.CharField(blank=True, db_comment='guarda la direccion de la empresa ', max_length=45, null=True)),
                ('telefono', models.CharField(blank=True, db_comment='guarda el contacto de la empresa ', max_length=45, null=True)),
                ('correo', models.CharField(blank=True, db_comment='guarda el correo de la empresa ', max_length=45, null=True)),
                ('razonsocial', models.CharField(blank=True, db_comment='guarda el nombre juridico de la empresa', max_length=45, null=True)),
                ('catgtall_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Factcabeza',
            fields=[
                ('idfactura', models.IntegerField(db_comment='guarda registro de factura ', primary_key=True, serialize=False)),
                ('cliente', models.CharField(blank=True, max_length=45, null=True)),
                ('fecha', models.CharField(blank=True, max_length=45, null=True)),
                ('valor_unitario', models.CharField(blank=True, db_column='valor unitario', max_length=45, null=True)),
                ('valortotal', models.CharField(blank=True, max_length=45, null=True)),
                ('pagos_tarjetacredito', models.IntegerField()),
                ('persona_idpersona', models.IntegerField()),
            ],
            options={
                'db_table': 'factcabeza',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Listadoempresaservicio',
            fields=[
                ('idlistadoempresaservicio', models.IntegerField(primary_key=True, serialize=False)),
                ('empresa_id', models.IntegerField()),
                ('servicio_idservicio', models.IntegerField()),
            ],
            options={
                'db_table': 'listadoempresaservicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='municipio',
            fields=[
                ('idmunicipio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('ciudad_idciudad', models.IntegerField()),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('idpersona', models.AutoField(db_comment='guarda  identificando individualmente el registro de cada persona.\n', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_comment='guarda el nombre del usuario ', max_length=45)),
                ('apellido', models.CharField(db_comment='guarda el apellido del usuario', max_length=45)),
                ('telefono', models.CharField(db_comment='guardara el contacto del usuario ', max_length=45)),
                ('correo', models.CharField(db_comment='guardara el correo del usuario', max_length=45)),
                ('contraseña', models.CharField(db_comment='guarda la contraseña del usuario', max_length=45)),
                ('tipersona_idtipersona', models.IntegerField()),
                ('municipio_idmunicipio', models.IntegerField()),
                ('genero', models.CharField(blank=True, max_length=45, null=True)),
                ('fechanacimiento', models.DateField(blank=True, null=True)),
                ('tdoc_idtdoc', models.IntegerField()),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pgos',
            fields=[
                ('idpgos', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
                ('factcabeza_idfactura', models.IntegerField()),
            ],
            options={
                'db_table': 'pgos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('idplanes', models.IntegerField(db_comment='guarda registro de cada plan \n', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, db_comment='guarda las promociones de cada taller \n', max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, db_comment='guarda el nombre del plan ', max_length=45, null=True)),
                ('servicio_idservicio', models.IntegerField()),
            ],
            options={
                'db_table': 'planes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Scripcion',
            fields=[
                ('idscripcion', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('valor', models.CharField(blank=True, max_length=45, null=True)),
                ('fecha', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'scripcion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idservicio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('cateserv_idcateserv', models.IntegerField()),
            ],
            options={
                'db_table': 'servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tdoc',
            fields=[
                ('idtdoc', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tdoc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipersona',
            fields=[
                ('idtipersona', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, db_comment='el usuario podra describir si es empresario. cliente o administrado de la aplicasion ', max_length=45, null=True)),
            ],
            options={
                'db_table': 'tipersona',
                'managed': False,
            },
        ),
    ]
