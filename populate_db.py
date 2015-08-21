#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Usuário administrador
db.auth_user.insert(**{
    'first_name': 'admin',
    'last_name': 'marolo',
    'email': 'marolo_admin@gmail.com',
    'password': 'pbkdf2(1000,20,sha512)$80f5803318b24f23$abdc38a233d2a8'\
    'c9fc611937c6269b2ab9c3ab46' # 123456
    })

# Notícias
for i in xrange(11):
    db.noticias.insert(**{
        'titulo': 'Lorem ipsum dolor sit amet, consectetur. {}'.format(i),
        'resumo': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'conteudo': '''
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro
        necessitatibus facere velit labore praesentium maxime ullam tenetur,
        numquam ut vero officiis nam distinctio. Accusantium, earum possimus.
        Tenetur reprehenderit, facilis. Culpa sunt voluptas, laborum deleniti
        assumenda, voluptatem eaque ullam incidunt, hic illo quisquam earum
        accusamus.
        Eveniet amet eos facilis, voluptatibus temporibus nam neque ab nemo,
        et ipsum commodi fuga quibusdam eum vero soluta itaque delectus cumque,
        quasi reprehenderit. Dignissimos natus consectetur fuga voluptatum ab sint,
        omnis dolorum deleniti cumque quis consequuntur esse pariatur repellendus
        ut voluptatem, consequatur dolorem et, rerum. Quibusdam aliquam ratione
        nihil nesciunt minus dolorem, velit aperiam optio tenetur!
        ''',
        'status': 'publicado',
        'created_by':1,
        'modified_by':1,
        })

# Membros
for i in xrange(11):
    db.membros.insert(**{
        'nome': 'Membro {}'.format(i),
        'email': 'membro{}@email.com'.format(i)
        })

# Eventos
for i in xrange(1, 11):
    ano = 2015
    if i%3 == 0:
        ano = 2014
    elif i%5 == 0:
        ano = 2013
    evento = {
        'nome': 'Evento {}'.format(i),
        'dia': '{}-08-{:02}'.format(ano, i),
        'horario_inicio': '09:{:02}:00'.format(i),
        'horario_fim': '18:00:00',
        'endereco': 'algum lugar',
        'descricao': '''Lorem ipsum dolor sit amet, consectetur adipisicing
        elit. Porro necessitatibus facere velit labore praesentium
        maxime ullam tenetur'
        '''
        }
    db.eventos.insert(**evento)

# Apoiadores
for i in range(10):
    tipo = 'patrocinador'
    if i > 5:
        tipo = 'apoaidor'
    elif i > 1:
        tipo = 'parceiro'
    db.apoiadores.insert(**{
        'nome': 'Apoiador {}'.format(i),
        'tipo': tipo,
        'url': 'https://en.wikipedia.org/wiki/Annona_crassiflora'
        })
