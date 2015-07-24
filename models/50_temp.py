#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon.contrib.populate import populate

CONTEUDO = '''
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Incidunt quia
beatae recusandae quos accusamus explicabo mollitia labore iusto nam nobis,
assumenda eius, accusantium nesciunt! A, molestiae vero dolor autem eligendi
natus, sunt cumque unde, accusamus totam aliquid perferendis modi.
Blanditiis!
'''
NUM_NOTICIAS = 10

if request.is_local:
    if db(db.noticias).count() == 0:
        for numero in range(NUM_NOTICIAS):
            db.noticias.insert(titulo='Título {}'.format(numero),
                               resumo='um resumo do texto',
                               conteudo=CONTEUDO, status='publicado')

    if db(db.apoiadores).count() == 0:
        db.apoiadores.insert(nome='Google', tipo='patrocinador',
                             url='http://google.com')
        db.apoiadores.insert(nome='Google', tipo='parceiro',
                             url='http://google.com')
        db.apoiadores.insert(nome='Google', tipo='parceiro',
                             url='http://google.com')
        db.apoiadores.insert(nome='Google', tipo='apoiador',
                             url='http://google.com')
        db.apoiadores.insert(nome='Google', tipo='apoiador',
                             url='http://google.com')

    if db(db.membros).count() == 0:
        populate(db.membros, 12)

    if db(db.eventos).count() == 0:
        populate(db.eventos, 10)
