import os, sys, glob
from shutil import copy2

# Runs to funcios to delete and populate the database
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

def setup():

	#if file does not exist in private directory copies into private folder
    if not os.path.exists('private/appconfig.ini'):
        try:
            copy2('./appconfig.ini', 'private/appconfig.ini')
        except:
            print('appconfig.ini not found')
   
    # Populates database
    if '-P' in sys.argv:
        populate_db()

    # Repopulates database
    if '-R' in sys.argv:
        repopulate_db()

    # Deletes database
    if '-D' in sys.argv:
        delete_db()


if __name__ == '__main__':
	setup()
    