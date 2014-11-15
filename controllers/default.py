# -*- coding: utf-8 -*-


def index():
    noticias = db(db.noticias.status == "publicado").select(
        orderby=~db.noticias.data_hora)
    return dict(noticias=noticias)


def noticias():
    noticia = db(db.noticias.permalink == request.args(0)).select().first()
    return dict(noticia=noticia)


def membros():
    return dict()


def projeto():
    sobre_projeto = XML(
        "<h1 class='text-center'>O que é o projeto?</h1>"
        "<p class='text-justify'>"
        "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, "
        "sed diam nonummy nibh euismod tincidunt ut laoreet dolore "
        "magna aliquam erat volutpat. Ut wisi enim ad minim veniam, "
        "quis nostrud exerci tation ullamcorper suscipit lobortis "
        "nisl ut aliquip ex ea commodo consequat. Duis autem vel eum "
        "iriure dolor in hendrerit in vulputate velit esse molestie "
        "consequat, vel illum dolore eu feugiat nulla facilisis at "
        "vero eros et accumsan et iusto odio dignissim qui blandit "
        "praesent luptatum zzril delenit augue duis dolore te feugait "
        "nulla facilisi."
        "</p>"
    )

    return dict(sobre_projeto=sobre_projeto)


def associacao():
    sobre_associacao = XML(
        "<h1 class='text-center'>O que é a associação?</h1>"
        "<p class='text-justify'>"
        "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, "
        "sed diam nonummy nibh euismod tincidunt ut laoreet dolore "
        "magna aliquam erat volutpat. Ut wisi enim ad minim veniam, "
        "quis nostrud exerci tation ullamcorper suscipit lobortis "
        "nisl ut aliquip ex ea commodo consequat. Duis autem vel eum "
        "iriure dolor in hendrerit in vulputate velit esse molestie "
        "consequat, vel illum dolore eu feugiat nulla facilisis at "
        "vero eros et accumsan et iusto odio dignissim qui blandit "
        "praesent luptatum zzril delenit augue duis dolore te feugait "
        "nulla facilisi."
        "</p>"
    )
    return dict(sobre_associacao=sobre_associacao)


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
