from gluon.contrib.populate import populate

if request.is_local:
    if db(db.noticias).count() == 0:
        populate(db.noticias, 10)
    if db(db.apoiadores).count() == 0:
        db.apoiadores.insert(nome='Google', tipo='patrocinador',
                             imagem='logo.png',
                             url='http://google.com')
        db.apoiadores.insert(nome='Google', tipo='parceiro',
                             imagem='logo.png',
                             url='http://google.com')
        db.apoiadores.insert(nome='Google', tipo='parceiro',
                             imagem='logo.png',
                             url='http://google.com')
        db.apoiadores.insert(nome='Google', tipo='apoiador',
                             imagem='logo.png',
                             url='http://google.com')
        db.apoiadores.insert(nome='Google', tipo='apoiador',
                             imagem='logo.png',
                             url='http://google.com')
    if db(db.membros).count() == 0:
        populate(db.membros, 12)
    if db(db.eventos).count() == 0:
        populate(db.eventos, 10)
