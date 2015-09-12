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


@auth.requires_membership('admin')
def register():
    db.auth_membership.user_id.writable = False
    db.auth_membership.user_id.readable = False
    form_register = SQLFORM.factory(
        db.auth_user,
        db.auth_membership,
        submit_button="Enviar"
    )

    if form_register.process().accepted:
        form_register.vars.user_id = db.auth_user.insert(
            **db.auth_user._filter_fields(form_register.vars)
        )
        db.auth_membership.insert(
            **db.auth_membership._filter_fields(form_register.vars)
        )
        response.flash = T('Usuário cadastrado com sucesso!')

    return dict(form_register=form_register)


@auth.requires_login()
def inserir():
    argumento = request.args(0) or redirect(URL('default', 'index'))
    lista_tabelas = ['noticias', 'eventos', 'produtos']
    if auth.has_membership('admin'):
        lista_tabelas.extend(['membros', 'apoiadores'])
    if argumento not in lista_tabelas:
        response.flash = T('Operação não permitida a seu usuário.')
        redirect(URL('admin', 'listar', args='noticias'))
    form = SQLFORM(
        db[argumento], submit_button="Enviar",
        formstyle='bootstrap3_stacked')
    if form.process().accepted:
        response.flash = 'Registro inserido com sucesso!'
    elif form.errors:
        response.flash = 'Formulário contem erros'
    return dict(argumento=argumento, form=form)


@auth.requires_login()
def listar():
    argumento = request.args(0) or redirect(URL('default', 'index'))
    lista_tabelas = ['noticias', 'eventos', 'produtos']
    if auth.has_membership('admin'):
        lista_tabelas.extend(['membros', 'apoiadores'])
    if argumento not in lista_tabelas:
        response.flash = T('Operação não permitida a seu usuário.')
        redirect(URL('admin', 'listar', args='noticias'))
    lista = db(db[argumento]).select(orderby=~db[argumento].id)
    return dict(argumento=argumento, lista=lista)


@auth.requires_login()
def editar():
    argumento = request.args(0) or redirect(URL('default', 'index'))
    lista_tabelas = ['noticias', 'eventos', 'produtos']
    if auth.has_membership('admin'):
        lista_tabelas.extend(['membros', 'apoiadores'])
    if argumento not in lista_tabelas:
        response.flash = T('Operação não permitida a seu usuário.')
        redirect(URL('admin', 'listar', args='noticias'))
    cod = request.args(1) or redirect(URL('default', 'index'))
    form = SQLFORM(
        db[argumento],
        cod,
        deletable=True,
        showid=False, submit_button="Enviar",
        upload=URL('default', 'download'), formstyle="bootstrap3_stacked"
    )

    if form.process().accepted:
        response.flash = 'Registro editado com sucesso'
    elif form.errors:
        response.flash = 'Formulário contem erros'
    return dict(argumento=argumento, form=form)
