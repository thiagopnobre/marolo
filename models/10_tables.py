# -*- coding: utf-8 -*-
# Notícias
db.define_table(
    'noticias',
    Field('titulo', length=128, notnull=True, unique=True),
    Field('resumo', length=128, notnull=True),
    Field('conteudo', 'text', length=5000, notnull=True),
    Field('permalink', notnull=True, unique=True),
    Field('foto', 'upload'),
    Field('thumbnail', 'upload'),
    Field('status'),
    auth.signature
)
# Membros
db.define_table(
    'membros',
    Field('nome', length=64, notnull=True, unique=True),
    Field('foto', 'upload'),
    Field('email', notnull=True)
)
# Eventos
db.define_table(
    'eventos',
    Field('nome', length=128, notnull=True),
    Field('dia', 'date', notnull=True),
    Field('horario_inicio', 'time', label=T('Inicio'), notnull=True),
    Field('horario_fim', 'time', label=T('Término'), notnull=True),
    Field('endereco', length=128, label=T('Endereço'), notnull=True),
    Field('descricao', length=256, label=T('Descrição'), notnull=True),
    Field('banner', 'upload'),
    Field('banner_thumb', 'upload')
)
# Apoiadores
db.define_table(
    'apoiadores',
    Field('nome', length=64, notnull=True),
    Field('tipo', notnull=True),
    Field('logo', 'upload'),
    Field('logo_thumb', 'upload'),
    Field('url', length=256, notnull=True),
)
