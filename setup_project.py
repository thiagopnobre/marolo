import os, glob, argparse
from shutil import copy2

# Runs to functions to delete and populate the database
def repopulate_db():
    delete_db()
    populate_db()

# Runs script to populate database
def populate_db():
    os.system("../../web2py.py -S marolo -M -R applications/marolo/populate_db.py")

# Deletes database files
def delete_db():
    files = glob.glob('./databases/*')
    for f in files:
        os.remove(f)

def copy_requirements():
    #if file does not exist in private directory copies into private folder
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

def setup():

    # adds arguments for terminal usage
    parser = argparse.ArgumentParser(prog='setup_project.py', description='Automatize project importing configs and handling database files.')
    parser.add_argument('-p', help='populate database', action="store_true")
    parser.add_argument('-d', help='delete database', action="store_true")
    parser.add_argument('-rp', help='repopulate database', action="store_true")
    parser.add_argument('-cp', help='copies dependences', action="store_true")

    # parse args
    args = parser.parse_args()

    # test arguments
    if args.p:
        populate_db()
        print('database populated.')

    if args.d:
        delete_db()
        print('database deleted.')

    if args.rp:
        repopulate_db()
        print('database repopulated.')

    if args.cp:
        copy_requirements()
        print('dependencies set')


if __name__ == '__main__':
    setup()
    