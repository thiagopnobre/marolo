apoiadores_geral = db(db.apoiadores).select()
parceiros = []
patrocinadores = []
apoiadores = []
for apoiador in apoiadores_geral:
    if apoiador.tipo == 'parceiro':
        parceiros.append(apoiador)
    elif apoiador.tipo == 'patrocinador':
        patrocinadores.append(apoiador)
    else:
        apoiadores.append(apoiador)
