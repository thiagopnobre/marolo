# -*- coding: utf-8 -*-
from gluon.tools import Auth
from gluon.tools import prettydate


db = DAL('sqlite://storage.sqlite', pool_size=1, check_reserved=['all'])

# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []

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
