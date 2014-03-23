# -*- coding: utf-8 -*-

def index():
    return dict()

def membros():
    return dict()

def projeto():
    return dict()

def eventos():
    return dict()

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

