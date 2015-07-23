# slug computado de noticias
db.noticias.permalink.compute = lambda registro: IS_SLUG()(registro.titulo)[0]
