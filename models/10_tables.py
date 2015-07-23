# modelo de dados
db.define_table(
    'noticias',
    Field('titulo', length=128, notnull=True, unique=True),
    Field('resumo', 'text', length=256, notnull=True),
    Field('conteudo', 'text', notnull=True),
    Field(
        'data_hora',
        'datetime',
        readable=False,
        writable=False,
        default=request.now,
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
