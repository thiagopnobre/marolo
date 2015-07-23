apoiadores_geral = db(db.apoiadores).select()
parceiros = [apoiador for apoiador in apoiadores_geral
             if apoiador.tipo == 'parceiro']
patrocinadores = [apoiador for apoiador in apoiadores_geral
                  if apoiador.tipo == 'patrocinador']
apoiadores = [apoiador for apoiador in apoiadores_geral
              if apoiador.tipo == 'apoiador']
