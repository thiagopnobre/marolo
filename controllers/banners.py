u"""Controlador responsável pelo controle do banner da tela inicial.

listar() - Retorna os banners de forma paginada.
altera_estado() - Alterna o estado de uma aba para ativa ou inativa
inserir() - Insere um novo banner
editar() - Edita um banner modificando seus atributos.
"""


@auth.requires_login()
def listar():
    """Lista os banners de forma paginada."""
    pagina = request.args(0, cast=int, default=1)
    itens_por_pagina = 10
    total = db(db.carousel).count()
    paginas = total / itens_por_pagina
    if total % itens_por_pagina:
        paginas += 1
    limites = (itens_por_pagina * (pagina - 1), (itens_por_pagina * pagina))
    banners = db(db.carousel).select(
        orderby=db.carousel.status | ~db.carousel.id,
        limitby=limites
    )
    return {
        'banners': banners,
        'pagina': pagina,
        'paginas': paginas,
    }


@auth.requires_login()
def altera_estado():
    """Altera o estado de uma aba do carousel.

    params:
        _id - id da aba
        estado - estado da aba, 0(inativo) ou 1(ativo)
    """
    _id = request.post_vars.id
    estado = request.post_vars.estado
    db(db.carousel.id == _id).update(status=estado)


@auth.requires_login()
def inserir():
    """Insere um novo banner."""
    form = SQLFORM(
        db.carousel, submit_button="Enviar",
        formstyle='bootstrap3_stacked')
    if form.process().accepted:
        response.flash = 'Registro inserido com sucesso!'
    elif form.errors:
        response.flash = 'Formulário contem erros'
    return dict(form=form)


@auth.requires_login()
def editar():
    """Edita um banner modificando seus atributos."""
    cod = request.args(0, cast=int, otherwise=URL('default', 'index'))
    form = SQLFORM(
        db.carousel,
        cod,
        deletable=True,
        showid=False, submit_button="Enviar",
        upload=URL('default', 'download'), formstyle="bootstrap3_stacked"
    )

    if form.process().accepted:
        session.flash = 'Registro editado com sucesso'
        redirect(URL('banners', 'listar'))
    elif form.errors:
        response.flash = 'Formulário contem erros'
    return dict(form=form)
