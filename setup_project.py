# -*- coding: utf-8 -*-

import os, glob, argparse
from shutil import copy2

# repovoa banco de dados
def repopulate_db():
    delete_db()
    populate_db()

# povoa banco de dados
def populate_db():
    os.system("../../web2py.py -S marolo -M -R ./applications/marolo/populate_db.py")

# apaga banco de dados
def delete_db():
    files = glob.glob('./databases/*')
    for f in files:
        os.remove(f)

# copia de requisitos (appconfig.ini e routes.py)
def copy_requirements():
    
    if not os.path.exists('private'):
        os.mkdir('private')

    if not os.path.exists('databases'):
        os.mkdir('databases')

    if not os.path.exists('private/appconfig.ini'):
        try:
            copy2('./appconfig.ini', 'private/appconfig.ini')
        except:
            print('appconfig.ini not found')

    if not os.path.exists('../../routes.py'):
        try:
            copy2('routes.py', '../../routes.py')
        except:
            print('routes.py not found')

# instalação de requisitos
def install_requirements():
    os.system("pip install -r requirements.txt")

def setup():

    # adição de argumentos para interface do terminal
    parser = argparse.ArgumentParser(prog='setup_project.py', description='Automatização do projeto importando configurações e banco de dados.')
    parser.add_argument('-p', help='povoar banco de dados', action="store_true")
    parser.add_argument('-d', help='apagar banco de dados', action="store_true")
    parser.add_argument('-rp', help='repovoar banco de dados', action="store_true")
    parser.add_argument('-cp', help='copiar dependências', action="store_true")
    parser.add_argument('-r', help='instalar dependências', action="store_true")

    # parse args
    args = parser.parse_args()

    if args.r:
        install_requirements()

    if args.cp:
        copy_requirements()
        print('dependencies set')

    # testa argumentos
    if args.p:
        populate_db()

    if args.d:
        delete_db()
        print('database deleted.')

    if args.rp:
        repopulate_db()
        print('database repopulated.')


if __name__ == '__main__':
    setup()
    
