# configure email
mail = auth.settings.mailer
mail.settings.server = myconf.take('smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')
