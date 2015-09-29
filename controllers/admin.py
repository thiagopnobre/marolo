import os


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


@auth.requires_membership('admin')
def listar_usuarios():
    lista = db(db.auth_user).select(orderby=~db.auth_user.id)
    return dict(lista=lista)


@auth.requires_membership('admin')
def editar_usuario():
    user_id = request.args(0, cast=int, otherwise=URL('default', 'index'))
    query = db.auth_user.id == user_id
    query &= db.auth_user.id == db.auth_membership.user_id
    user_data = db(query).select(
        db.auth_user.first_name,
        db.auth_user.last_name,
        db.auth_user.email,
        db.auth_membership.group_id,
    ).first()

    for campo, valor in user_data.auth_user.items():
        db.auth_user[campo].default = valor
    for campo, valor in user_data.auth_membership.items():
        db.auth_membership[campo].default = valor
    db.auth_user.email.requires = IS_EMAIL(error_message=T('Email inválido!'))
    db.auth_user.password.writable = False
    db.auth_user.password.readable = False
    db.auth_membership.user_id.writable = False
    db.auth_membership.user_id.readable = False
    form_update = SQLFORM.factory(
        db.auth_user,
        db.auth_membership,
        Field('apagar', 'boolean', default=False, label='Marque para apagar'),
        submit_button="Enviar"
    )

    if form_update.process().accepted:
        if form_update.vars.apagar:
            db(db.auth_user.id == user_id).delete()
            db(db.auth_membership.user_id == user_id).delete()
            session.flash = T('Usuário apagado com sucesso!')
            redirect(URL('admin', 'listar_usuarios'))

        db(db.auth_user.id == user_id).update(
            **db.auth_user._filter_fields(form_update.vars)
        )
        db(db.auth_membership.user_id == user_id).update(
            **db.auth_membership._filter_fields(form_update.vars)
        )
        session.flash = T('Usuário editado com sucesso!')
        redirect(URL('admin', 'listar_usuarios'))

    return dict(form_update=form_update)


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
        session.flash = 'Registro editado com sucesso'
        redirect(URL('admin', 'listar', args=argumento))
    elif form.errors:
        response.flash = 'Formulário contem erros'
    return dict(argumento=argumento, form=form)


@auth.requires_membership('admin')
def associacao():
    path = os.path.dirname(os.path.abspath(__file__))
    with open(path + '/../views/default/sobre_associacao.html', 'r') as arq:
        sobre_associacao = arq.read()
    form = SQLFORM.factory(
        Field(
            'texto',
            'text',
            widget=ckeditor.widget,
            default=sobre_associacao,
            requires=IS_NOT_EMPTY()
        ),
        hideerror=True,
        message_onfailure=T('O conteúdo não pode ser vazio.')
    )
    form.elements('label', replace=None)
    if form.process().accepted:
        with open(path + '/../views/default/sobre_associacao.html',
                  'w') as arq:
            arq.write(form.vars.texto)
        session.flash = T('Sobre a associação editado com sucesso!')
        redirect(URL('admin', 'listar', args='noticias'))
    return {'form': form}


@auth.requires_membership('admin')
def projeto():
    path = os.path.dirname(os.path.abspath(__file__))
    with open(path + '/../views/default/sobre_projeto.html', 'r') as arq:
        sobre_projeto = arq.read()
    form = SQLFORM.factory(
        Field(
            'texto',
            'text',
            widget=ckeditor.widget,
            default=sobre_projeto,
            requires=IS_NOT_EMPTY()
        ),
        hideerror=True,
        message_onfailure=T('O conteúdo não pode ser vazio.')
    )
    form.elements('label', replace=None)
    if form.process().accepted:
        with open(path + '/../views/default/sobre_projeto.html',
                  'w') as arq:
            arq.write(form.vars.texto)
        session.flash = T('Sobre o projeto editado com sucesso!')
        redirect(URL('admin', 'listar', args='noticias'))
    return {'form': form}
