#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datas.functions_datas import select_query

import sqlite3

class installation :

    def __init__(self, NUMERO_INSTALLATON, NOM_INSTALLATIONS, NOM_COMMUNE, CODE_POSTAL, NUMERO_VOIE, NOM_VOIE):

        self.NOM_INSTALLATIONS = NOM_INSTALLATIONS
        self.NUMERO_INSTALLATON = NUMERO_INSTALLATON
        self.CODE_POSTAL = CODE_POSTAL
        self.NUMERO_VOIE = NUMERO_VOIE
        self.NOM_VOIE = NOM_VOIE
        self.NOM_COMMUNE = NOM_COMMUNE

    def add_installation(self, conn):
        """ Permet d'ajouter une installation dans la base de donnée
            :argument
                :parameter: conn correspond au cursor de la connexion en cours
        """

        insertQuery = "INSERT INTO installations(NUMERO_INSTALLATON, NOM_INSTALLATIONS, NOM_COMMUNE, CODE_POSTAL, NUMERO_VOIE, NOM_VOIE)\
                                                    VALUES(?,?,?,?,?,?)"
        conn.execute(insertQuery, ( self.NUMERO_INSTALLATON, self.NOM_INSTALLATIONS, self.NOM_COMMUNE, self.CODE_POSTAL, self.NUMERO_VOIE, self.NOM_VOIE))

def create_object_installation(id_installation, name_installation, town, zip, num_street, name_street):
    """
        Permet, grâce à la base de données, de créer un ou des nouveaux objects installations
        Pour filtrer les objects à récupérer, il suffit de mettre 'None' pour les attributs qui ne nous interresse pas
        :argument:
            :parameter: id_installation
            :parameter: name_installation
            :parameter: town
            :parameter: zip
            :parameter: num_street
            :parameter: name_street
    """

    #Je me connecte à ma base pour récupérer l'objet en question.
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    list_conditions = []

    #Je récupère les conditions pour la base de données, que j'insère ensuite dans la liste list_conditions
    if id_installation != None :
        list_conditions.append(" NUMERO_INSTALLATON = " + id_installation)
    if name_installation != None :
        list_conditions.append(" NOM_INSTALLATIONS LIKE '%{}%'".format(name_installation))
    if town != None :
        list_conditions.append(" NOM_COMMUNE LIKE '%{}%'".format(town))
    if zip != None :
        list_conditions.append(" CODE_POSTAL LIKE '%{}%'".format(zip))
    if num_street != None :
        list_conditions.append(" NUMERO_VOIE = " + num_street)
    if name_street != None :
        list_conditions.append(" NOM_VOIE LIKE '%{}%'".format(name_street))

    #Je récupère ma requête à exécuter
    query = select_query('installations', list_conditions)
    c.execute(query)

    list = []
    #Je parcours toute les lignes récupérées, et je crée pour chacune un objet
    for row in c :
        #Je créer mon objet puis je le stocke dans un dictionnaire avec pour clé le numéro d'installation
        obj = installation(row[0],row[1],row[2],row[3],row[4],row[5])
        list.append(obj)

    conn.close()
    return list


