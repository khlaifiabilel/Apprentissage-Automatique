#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ici, on va utiliser des outils existants
# Et programmer le reste (ce qu'on a pas pu trouver dans ces outils)
# Le but est de se familiariser avec ces outils

import pandas
import sqlite3
import numpy
from lxml import etree

#lire le premier fichier (CSV)
adult1 = pandas.read_csv("../../data/adult1.csv", skipinitialspace=True)

#lire le deuxième fichier (CSV)
#     - séparateur (;)
#     - pas d'entête (la première ligne contient des données)
noms = ["class", "age", "sex", "workclass", "education", "hours-per-week", "marital-status"]
adult2 = pandas.read_csv("../../data/adult2.csv", skipinitialspace=True, sep=";", header=None, names=noms)

#lire les données à partir d'un fichier Sqlite
#Les ? doivent être Considérées comme des NaN
con = sqlite3.connect("../../data/adult3.db")
adult3 = pandas.read_sql_query("SELECT * FROM income", con)
adult3 = adult3.replace('?', numpy.nan)

#valider le fichier XML
parser = etree.XMLParser(dtd_validation=True)
arbre = etree.parse("../../data/adult4.xml", parser)

adult4 = pandas.DataFrame(columns=noms)

for candidat in arbre.getroot():
    id = candidat.
    print candidat.tag
    #adult4 = adult4.append(pandas.Series([i.get('id'), i.get('name')], index=dfcols), ignore_index=True)
adult4.head()