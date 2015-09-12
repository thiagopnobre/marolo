default_application = 'marolo'
default_controller = 'default'
default_function = 'index'

routes_in = (
    (r'/index', r'/marolo/default/index'),
    (r'/index/$pagina', r'/marolo/default/index/$pagina'),
    (r'/noticias/$permalink', r'/marolo/default/noticias/$permalink'),
    (r'/membros', r'/marolo/default/membros'),
    (r'/projeto', r'/marolo/default/projeto'),
    (r'/associacao', r'/marolo/default/associacao'),
    (r'/produtos', r'/marolo/default/produtos'),
    (r'/produtos/$pagina', r'/marolo/default/produtos/$pagina'),
    (r'/eventos', r'/marolo/default/eventos'),
    (r'/eventos/$ano', r'/marolo/default/eventos/$ano'),
    (r'/contato', r'/marolo/default/contato'),
    (r'/admin', r'/marolo/admin/user/login'),
    (r'/admin/register', r'/marolo/admin/register'),
    (r'/admin/$action', r'/marolo/admin/user/$action'),
    (r'/admin/inserir/$argumento', r'/marolo/admin/inserir/$argumento'),
    (r'/admin/listar/$argumento', r'/marolo/admin/listar/$argumento'),
    (r'/admin/editar/$argumento/$cod',
     r'/marolo/admin/editar/$argumento/$cod'),
    (r'/static/images/(?P<imagem>[\w./-]+)',
     r'/marolo/static/images/\g<imagem>'),
)

routes_out = (
    (r'/marolo/default/index', r'/index'),
    (r'/marolo/default/index/$pagina', r'/index/$pagina'),
    (r'/marolo/default/noticias/$permalink', r'/noticias/$permalink'),
    (r'/marolo/default/membros', r'/membros'),
    (r'/marolo/default/projeto', r'/projeto'),
    (r'/marolo/default/associacao', r'/associacao'),
    (r'/marolo/default/produtos', r'/produtos'),
    (r'/marolo/default/produtos/$pagina', r'/produtos/$pagina'),
    (r'/marolo/default/eventos', r'/eventos'),
    (r'/marolo/default/eventos/$ano', r'/eventos/$ano'),
    (r'/marolo/default/contato', r'/contato'),
    (r'/marolo/admin/user/login', r'/admin'),
    (r'/marolo/admin/register', r'/admin/register'),
    (r'/marolo/admin/user/$action', r'/admin/$action'),
    (r'/marolo/admin/inserir/$argumento', r'/admin/inserir/$argumento'),
    (r'/marolo/admin/listar/$argumento', r'/admin/listar/$argumento'),
    (r'/marolo/admin/editar/$argumento/$cod',
     r'/admin/editar/$argumento/$cod'),
    (r'/marolo/static/images/\g<imagem>',
     r'/static/images/(?P<imagem>[\w./-]+)'),
)
