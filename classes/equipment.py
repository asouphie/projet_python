#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.fonctions_generales import select_query

import sqlite3

class equipment :
    def __init__(self, ID_EQUIPEMENTS, NOM_EQUIPEMENTS, NUMERO_INSTALLATION):
        self.NUMERO_INSTALLATION = NUMERO_INSTALLATION
        self.ID_EQUIPEMENTS = ID_EQUIPEMENTS
        self.NOM_EQUIPEMENTS = NOM_EQUIPEMENTS

    """ Permet d'ajouter un équipement dans la base de donnée """

    def add_equipment(self, conn):
        insertQuery = "INSERT INTO equipement(ID_EQUIPEMENTS, NOM_EQUIPEMENTS, NUMERO_INSTALLATION) VALUES(?,?,?)"
        conn.execute(insertQuery, (self.ID_EQUIPEMENTS, self.NOM_EQUIPEMENTS, self.NUMERO_INSTALLATION))


"""
    Permet, grâce à la base de données, de créer un ou des nouveaux objets équipements
    Pour filtrer les objets à récupérer, il suffit de mettre 'None' pour les attributs qui ne nous interresse pas
"""
def create_equipment(idEquipment, numInstallation, nameEquipment):
    #Je me connecte à ma base pour récupérer l'objet en question.
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    listConditions = []

    # Je récupère les conditions pour la base de données, que j'insère ensuite dans la liste list_conditions
    if idEquipment != None :
        listConditions.append(" ID_EQUIPEMENTS = " + idEquipment)
    if numInstallation != None :
        listConditions.append(" NUMERO_INSTALLATION = " + numInstallation)
    if nameEquipment != None :
        listConditions.append(" NOM_EQUIPEMENTS LIKE " + nameEquipment)
    # Je récupère ma requête à exécuter
    query = select_query('equipement', listConditions)
    c.execute(query)

    list = []
    # Je parcours toute les lignes récupérées, et je crée pour chacune un objet
    for row in c :
        # Je créer mon objet puis je le stocke dans un dictionnaire avec pour clé le numéro d'équipement
        obj = equipment(row[0], row[1], row[2])
        list.append(obj)

    conn.close()
    return list