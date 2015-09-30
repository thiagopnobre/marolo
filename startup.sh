#!/bin/bash
mkdir private -p
mkdir databases -p
pip install -U -r requirements.txt
cp ./appconfig.ini  private/
cp routes.py ../../
rm -f databases/*
python ../../web2py.py -S marolo -M -R ./applications/marolo/populate_db.py

