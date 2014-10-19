# -*- coding: utf-8 -*-

db = DAL('sqlite://storage.sqlite', pool_size=1, check_reserved=['all'])

# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []

from gluon.tools import Auth
auth = Auth(db, controller='admin', function='user')

# create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

# configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# auth settings
auth.settings.login_next = URL('admin','listar',args=['noticias'])
auth.settings.logout_next = URL('default','index')
from gluon.tools import prettydate

# modelo de dados
db.define_table(
    'noticias',
    Field('titulo', length=128, notnull=True, unique=True),
    Field('resumo','text', length=256, notnull=True),
    Field('conteudo', 'text', notnull=True),
    Field(
        'data_hora',
        'datetime',
        default=request.now,
        notnull=True
    ),
    Field(
        'permalink',
        notnull=True,
        unique=True,
    ),
    Field(
        'foto',
        'upload',
        requires=IS_EMPTY_OR(IS_IMAGE(error_message='Insira uma imagem!'))
    ),
    Field(
        'status',
        requires=IS_IN_SET(['publicado', 'não publicado'])
    )
)

db.define_table(
    'membros',
    Field('nome', length=64, notnull=True),
    Field(
        'foto',
        'upload',
        requires=IS_EMPTY_OR(IS_IMAGE(error_message='Insira uma imagem!'))
    ),
    Field('email', requires=IS_EMAIL())
)

db.define_table(
    'projeto',
    Field('nome', length=64, notnull=True),
    Field('email', requires=IS_EMAIL(), notnull=True),
    Field('sobre', 'text', notnull=True)
)

db.define_table(
    'associacao',
    Field('nome', length=64, notnull=True),
    Field('email', requires=IS_EMAIL(), notnull=True),
    Field('sobre', 'text', notnull=True)
)

db.define_table(
    'eventos',
    Field('nome', length=128),
    Field(
        'data_hora',
        'datetime',
        default=request.now,
        notnull=True
    ),
    Field('localizacao', notnull=True),
    Field('descricao', 'text', notnull=True),
    Field(
        'banner',
        'upload',
        requires=IS_EMPTY_OR(IS_IMAGE(error_message='Insira uma imagem!'))
    )
)

db.define_table(
    'apoiadores',
    Field('nome', length=64, notnull=True),
    Field(
        'tipo',
        length=64,
        requires=IS_IN_SET(['patrocinador', 'parceiro', 'apoiador'])
    ),
    Field('imagem', 'upload', notnull=True),
    Field('url', requires=IS_URL(), notnull=True)
)



# Plugin
from plugin_ckeditor import CKEditor
ckeditor = CKEditor(db)
ckeditor.define_tables()
db.projeto.sobre.widget = ckeditor.widget
db.noticias.conteudo.widget = ckeditor.widget
db.associacao.sobre.widget = ckeditor.widget
db.eventos.descricao.widget = ckeditor.widget
db.noticias.permalink.compute = lambda registro:IS_SLUG()(registro.titulo)[0]
auth.settings.formstyle = 'bootstrap3_stacked'

parceiros = db(db.apoiadores.tipo == 'parceiro').select()
apoiadores = db(db.apoiadores.tipo == 'apoiador').select()
patrocinadores = db(db.apoiadores.tipo == 'patrocinador').select()


