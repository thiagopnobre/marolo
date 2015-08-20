# coding: utf-8
from smarthumb import SMARTHUMB
from gluon.contrib.imageutils import RESIZE

# Noticias
db.noticias.titulo.requires = [
    IS_NOT_EMPTY(error_message=T('Este campo não pode ficar vazio!')),
    IS_NOT_IN_DB(db, db.noticias.titulo,
                 error_message=T('Título deve ser único.')),
    IS_LENGTH(128, error_message=T('Tamanho máximo de 128 caracteres.'))
]
db.noticias.resumo.requires = [
    IS_NOT_EMPTY(
        error_message=T('Este campo não pode ficar vazio!')),
    IS_LENGTH(128, error_message=T('Tamanho máximo de 128 caracteres.'))
]
db.noticias.conteudo.requires = [
    IS_NOT_EMPTY(
        error_message=T('Este campo não pode ficar vazio!')),
    IS_LENGTH(5000, error_message=T('Tamanho máximo de 5000 caracteres.'))
]
db.noticias.permalink.compute = lambda registro: IS_SLUG()(registro.titulo)[0]
db.noticias.foto.requires = [
    IS_EMPTY_OR(IS_IMAGE(
        error_message=T('Arquivo enviado deve ser uma imagem.'))),
    IS_LENGTH(100 * 1024,  # 100kb
              error_message=T('Arquivo muito grande!'
                              'Tamanho máximo permitido é 100kb'))
]
db.noticias.thumbnail.compute = lambda registro: SMARTHUMB(registro.foto,
                                                           (200, 200))
db.noticias.status.requires = IS_IN_SET(
    ['publicado', 'não publicado'],
    error_message=T('Por favor selecione uma das opções')
)

# Membros
db.membros.nome.requires = [
    IS_NOT_EMPTY(error_message=T('Este campo não pode ficar vazio!')),
    IS_NOT_IN_DB(db, db.membros.nome,
                 error_message=T('Nome deve ser único.')),
    IS_LENGTH(64, error_message=T('Tamanho máximo de 64 caracteres.'))
]
db.membros.foto.requires = [
    IS_EMPTY_OR(
        IS_IMAGE(error_message=T('Arquivo enviado deve ser uma imagem.'))
    ),
    IS_LENGTH(100 * 1024,  # 100kb
              error_message=T('Arquivo muito grande!'
                              'Tamanho máximo permitido é 100kb')),
    IS_EMPTY_OR(RESIZE(200, 200))
]
db.membros.email.requires = IS_EMAIL(error_message=T("Entre um email válido"))

# Eventos
db.eventos.nome.requires = [
    IS_NOT_EMPTY(error_message=T('Este campo não pode ficar vazio!')),
    IS_LENGTH(128, error_message=T('Tamanho máximo de 128 caracteres.'))
]
db.eventos.endereco.requires = [
    IS_NOT_EMPTY(error_message=T('Este campo não pode ficar vazio!')),
    IS_LENGTH(128, error_message=T('Tamanho máximo de 128 caracteres.'))
]
db.eventos.descricao.requires = [
    IS_NOT_EMPTY(error_message=T('Este campo não pode ficar vazio!')),
    IS_LENGTH(256, error_message=T('Tamanho máximo de 256 caracteres.'))
]
db.eventos.banner.requires = [
    IS_EMPTY_OR(IS_IMAGE(
        error_message=T('Arquivo enviado deve ser uma imagem.'))),
    IS_LENGTH(100 * 1024,  # 100kb
              error_message=T('Arquivo muito grande!'
                              'Tamanho máximo permitido é 100kb'))
]
db.eventos.banner_thumb.compute = lambda registro: SMARTHUMB(registro.foto,
                                                             (200, 200))

# Apoiadores
db.apoiadores.nome.requires = [
    IS_NOT_EMPTY(error_message=T('Este campo não pode ficar vazio!')),
    IS_LENGTH(64, error_message=T('Tamanho máximo de 64 caracteres.'))
]
db.apoiadores.tipo.requires = IS_IN_SET(
    ['apoiador', 'patrocinador', 'parceiro'],
    error_message=T('Por favor selecione uma das opções')
)
db.apoiadores.logo.requires = [
    IS_EMPTY_OR(
        IS_IMAGE(error_message=T('Arquivo enviado deve ser uma imagem.'))
    ),
    IS_LENGTH(100 * 1024,  # 100kb
              error_message=T('Arquivo muito grande!'
                              'Tamanho máximo permitido é 100kb'))
]
db.apoiadores.logo_thumb.compute = lambda registro: SMARTHUMB(registro.logo,
                                                              (200, 200))
db.apoiadores.url.requires = [
    IS_NOT_EMPTY(error_message=T('Este campo não pode ficar vazio!')),
    IS_LENGTH(256, error_message=T('Tamanho máximo de 256 caracteres.')),
    IS_URL()
]
