from plugin_ckeditor import CKEditor

# Plugin
ckeditor = CKEditor(db)
ckeditor.define_tables()
db.noticias.conteudo.widget = ckeditor.widget
db.eventos.descricao.widget = ckeditor.widget
