def index():
    redirect(URL(c='admin', f='user'))

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@auth.requires_login()
def inserir():
    argumento = request.args(0) or redirect(URL('default', 'index'))
    if argumento not in ('noticias', 'membros', 'eventos', 'apoiadores'):
        redirect(URL('default', 'index'))
    form = SQLFORM(
        db[argumento], submit_button="Enviar", formstyle='bootstrap3_stacked')
    if form.process().accepted:
        response.flash = 'Registro inserido com sucesso!'
    elif form.errors:
        response.flash = 'Formulário contem erros'
    return dict(argumento=argumento, form=form)


@auth.requires_login()
def listar():
    argumento = request.args(0) or redirect(URL('default', 'index'))
    if argumento not in ('noticias', 'membros', 'eventos', 'apoiadores'):
        redirect(URL('default', 'index'))
    lista = db(db[argumento]).select()
    return dict(argumento=argumento, lista=lista)


@auth.requires_login()
def editar():
    argumento = request.args(0) or redirect(URL('default', 'index'))
    if argumento not in ('noticias', 'membros', 'eventos', 'apoiadores',
                         'projeto', 'associacao'):
        redirect(URL('default', 'index'))
    cod = request.args(1) or redirect(URL('default', 'index'))
    form = SQLFORM(
        db[argumento],
        cod,
        deletable=argumento not in ('projeto', 'associacao'),
        showid=False, submit_button="Enviar",
        formstyle="bootstrap3_stacked"
    )

    if form.process().accepted:
        response.flash = 'Registro editado com sucesso'
    elif form.errors:
        response.flash = 'Formulário contem erros'
    return dict(argumento=argumento, form=form)
