# -*- coding: utf-8 -*-
u"""Controlador responsável pelo controle das telas de navegação do site.

index() - Exibe a tela inicial com banner e notícias.
noticias() - Exibe uma notícia.
membros() - Exibe uma lista de membros.
associacao() - Exibe uma descrição sobre a associação.
projeto() - Exibe uma descrição sobre o projeto.
eventos() - Exibe os eventos em uma timeline.
contato() - Exibe um formulário para contato.
produtos() - Exibe uma lista de produtos de forma paginada.
download() - Permite o download de arquivos enviados.
"""


def index():
    """Retorna os banners e as notícias da tela inicial, em ordem decrescente e
     de forma paginada.
    """
    pagina = request.args(0, cast=int, default=1)
    itens_por_pagina = 5
    total = db(db.noticias).count()
    paginas = total / itens_por_pagina
    if total % itens_por_pagina:
        paginas += 1
    limites = (itens_por_pagina * (pagina - 1), (itens_por_pagina * pagina))
    noticias = db(db.noticias.status == "publicado").select(
        orderby=~db.noticias.created_on | ~db.noticias.modified_on,
        limitby=limites
    )
    carousel = db(db.carousel.status == 'ativo').select(
        orderby=~db.carousel.id,
        limitby=(0, 4),
    )
    return {
        'noticias': noticias,
        'pagina': pagina,
        'paginas': paginas,
        'carousel': carousel
    }


def noticias():
    """Retorna a notícia a ser exibida"""
    permalink = request.args(0, otherwise='/')
    noticia = db.noticias(permalink=permalink)
    if not noticia:
        session.flash = T('Desculpe, não existem noticias cadastradas ainda')
        redirect('/')
    return dict(noticia=noticia)


def membros():
    """Retorna a lista de membros cadastrados em formato de uma matriz N x 3."""
    membros = db(db.membros).select().as_list()
    if not membros:
        session.flash = T('Desculpe, não existem membros cadastrados ainda')
        redirect('/')
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
    """Exibe uma descrição sobre a associação."""
    return {}


def projeto():
    """Exibe uma descrição sobre o projeto."""
    return {}


def eventos():
    """Retorna os eventos do ano atual ou do ano solicitado, o ano dos eventos a
    serem exibidos, uma lista de anos anteriores e uma lista de anos posteriores,
    para que os eventos possam ser exibidos em tela.
    """
    parametro_ano = request.args(0, cast=int, default=request.now.year)
    ano_atual = request.now.year
    eventos = db(db.eventos.dia.year() == parametro_ano).select()
    if not eventos:
        session.flash = T('Desculpe, não existem eventos cadastrados ainda')
        redirect('/')
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
    """Retorna um formulário de contato, que se for válido, envia um e-mail de
    contato para o e-mail definido em appconfig.ini."""
    if form.validate():
        campos = form.vars
        mail.send(
            to=mail.settings.sender,
            subject=campos['assunto'],
            message=campos['mensagem'],
            sender=campos['email']
        )
    return dict(form=form)


def produtos():
    """Exibe uma lista de produtos de forma paginada, com 9 itens por página."""
    pagina = request.args(0, cast=int, default=1)
    itens_por_pagina = 9
    total = db(db.produtos).count()
    if not total:
        session.flash = T('Desculpe, não existem produtos cadastrados ainda')
        redirect('/')
    paginas = total / itens_por_pagina
    if total % itens_por_pagina:
        paginas += 1
    limites = (itens_por_pagina * (pagina - 1), (itens_por_pagina * pagina))
    produtos = db(db.produtos).select(
        limitby=limites
    )
    return {
        'produtos': produtos,
        'pagina': pagina,
        'paginas': paginas
    }


@cache.action()
def download():
    """
    Allow downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
