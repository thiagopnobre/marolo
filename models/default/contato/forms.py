form = SQLFORM.factory(
    Field(
        'email',
        requires=IS_EMAIL(
            error_message=T('Entre com um endereço de email válido.'),
        ),
    ),
    Field('assunto', requires=IS_IN_SET(
        [
            T('Reclamações'), T('Sugestões'),
            T('Parceria'), T('Outros')
        ],
        zero=T('Escolha um assunto'),
        error_message=T('Deve escolher uma opção.')
    ),
    ),

    Field('mensagem', 'text', requires=IS_NOT_EMPTY(
        error_message=T('Por favor escreva um texto.')),
    ),
    submit_button=T('Enviar'),
    formstyle='bootstrap3_inline',
    _class='form-horizontal'
)
form.element(_name="email").update(
    _placeholder='Email',
    _required=''
)
form.element(_name='mensagem').update(
    _placeholder=T('Digite aqui sua mensagem.'),
    _required='',
    _rows='4'
)
