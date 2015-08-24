# -*- coding: utf-8 -*-
from default.contato.forms import form_contato


def index():
    noticias = db(db.noticias.status == "publicado").select()
    return dict(noticias=noticias)


def noticias():
    noticia = db(db.noticias.permalink == request.args(0)).select().first()
    return dict(noticia=noticia)


def membros():
    membros = db(db.membros).select().as_list()
    linhas = (len(membros) // 3) + 1
    matriz = []
    for _ in range(linhas):
        aux = []
        cont = 0
        while cont < 3 and membros:
            aux.append(membros.pop(0))
            cont += 1
        matriz.append(aux)
    return {
        'matriz': matriz
    }


def associacao():
    return {}


def projeto():
    return {}


def eventos():
    parametro_ano = request.args(0, cast=int, default=request.now.year)
    ano_atual = request.now.year
    eventos = db(db.eventos.dia.year() == parametro_ano).select()
    minimo = db.eventos.dia.min()
    maximo = db.eventos.dia.max()
    extremos = db().select(maximo, minimo).first()
    menor_ano = extremos[minimo].year
    maior_ano = extremos[maximo].year
    anos_anteriores = []
    anos_posteriores = []
    for incremento in range(3, 0, -1):
        ano_posterior = parametro_ano + incremento
        if (ano_posterior <= maior_ano) or (ano_posterior <= ano_atual):
            anos_posteriores.append(ano_posterior)
    for subtrator in range(1, 4):
        ano_anterior = parametro_ano - subtrator
        if ano_anterior >= menor_ano:
            anos_anteriores.append(ano_anterior)
    return {
        'eventos': eventos,
        'ano': parametro_ano,
        'anos_anteriores': anos_anteriores,
        'anos_posteriores': anos_posteriores,
    }


def contato():
    form = form_contato()
    if form.validate():
        campos = form.vars
        mail.send(
            to=mail.settings.sender,
            subject=campos['assunto'],
            message=campos['mensagem'],
            sender=campos['email']
        )
    return dict(form=form)


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
