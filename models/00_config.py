# -*- coding: utf-8 -*-
from gluon.tools import Auth
from gluon.tools import prettydate
from gluon.contrib.appconfig import AppConfig

# app configuration made easy. Look inside private/appconfig.ini
# once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)

db = DAL(
    myconf.take('db.uri'),
    pool_size=myconf.take('db.pool_size', cast=int),
    check_reserved=['all'],
    migrate=myconf.take('db.migrate', cast=bool)
)

response.formstyle = myconf.take('forms.formstyle')
response.form_label_separator = myconf.take('forms.separator')


# AUTH
auth = Auth(db, controller='admin', function='user')

# create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

# configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# auth settings
auth.settings.login_next = URL('admin', 'listar', args=['noticias'])
auth.settings.logout_next = URL('default', 'index')
auth.settings.actions_disabled = ['register']
auth.settings.remember_me_form = False

auth.settings.formstyle = 'bootstrap3_stacked'

# Language force for pt-br
T.force('pt-br')

# Don't use generic views
response.generic_patterns = []
