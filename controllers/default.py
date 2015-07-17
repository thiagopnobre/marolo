# -*- coding: utf-8 -*-


def index():
    noticias = db(db.noticias.status == "publicado").select(
        orderby=~db.noticias.data_hora)
    return dict(noticias=noticias)


def noticias():
    noticia = db(db.noticias.permalink == request.args(0)).select().first()
    return dict(noticia=noticia)


def membros():
    membros = db(db.membros).select()
    linhas = (len(membros) % 3) or 1
    return {
        'membros': membros,
        'linhas': linhas
    }


def eventos():
    return dict()


def contato():
    # TODO: feedback user
    form = FORM(
        P(
            INPUT(
                _name='email',
                _class='email',
                _type="email",
                _placeholder="Email",
                _required='true'
            )
        ),
        P(
            INPUT(
                _name="assunto",
                _class="assunto",
                _type="text",
                _placeholder="Assunto",
                _required='true'
            )
        ),
        P(
            TEXTAREA(
                _name="mensagem",
                _class="mensagem",
                _placeholder="Mensagem",
                _rows="4",
                _required='true'
            )
        ),
        P(
            BUTTON(
                I(_class="fa fa-envelope-o"),
                " Enviar",
                _class="btn btn-success btn-contato",
                _type="submit"
            )
        )
    )
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
