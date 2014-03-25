# -*- coding: utf-8 -*-

def index():
    return dict()

def membros():
    return dict()

def projeto():
    sobre_projeto = XML("<h1 class='text-center'>O que é o projeto?</h1>"
                        "<p class='text-justify'>"
                        "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, "
                        "sed diam nonummy nibh euismod tincidunt ut laoreet dolore "
                        "magna aliquam erat volutpat. Ut wisi enim ad minim veniam, "
                        "quis nostrud exerci tation ullamcorper suscipit lobortis "
                        "nisl ut aliquip ex ea commodo consequat. Duis autem vel eum "
                        "iriure dolor in hendrerit in vulputate velit esse molestie "
                        "consequat, vel illum dolore eu feugiat nulla facilisis at "
                        "vero eros et accumsan et iusto odio dignissim qui blandit "
                        "praesent luptatum zzril delenit augue duis dolore te feugait "
                        "nulla facilisi."
                        "</p>")
    return dict(sobre_projeto=sobre_projeto)

def eventos():
    return dict()

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

