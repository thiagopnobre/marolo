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
            _class="btn btn btn-success btn-contato",
            _type="submit"
        )
    )
)
