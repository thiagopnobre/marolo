# -*- coding: utf-8 -*-

def index():
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

