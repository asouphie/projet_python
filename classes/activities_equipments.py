#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.fonctions_generales import select_query

import sqlite3

class activities_equipments :
    def __init__(self, ID_EQUIPEMENTS, ID_ACTIVITES, NOM_ACTIVITES, NIVEAU_ACTIVITE):
        self.ID_EQUIPEMENTS = ID_EQUIPEMENTS
        self.ID_ACTIVITES = ID_ACTIVITES
        self.NOM_ACTIVITES = NOM_ACTIVITES
        self.NIVEAU_ACTIVITE = NIVEAU_ACTIVITE


    """
        Permet d'ajouter une activité dans la base de donnée
    """
    def add_activities_equipments(self, conn):
        insertQuery = "INSERT INTO equipements_activites(ID_EQUIPEMENTS, ID_ACTIVITES, NOM_ACTIVITES, " \
                      "NIVEAU_ACTIVITE) VALUES(?,?,?,?)"
        conn.execute(insertQuery, (self.ID_EQUIPEMENTS, self.ID_ACTIVITES,
                           self.NOM_ACTIVITES, self.NIVEAU_ACTIVITE))


"""
    Permet, grâce à la base de données, de créer un ou des nouveaux objets activités_equipements .
    Pour filtrer les objets à récupérer, il suffit de mettre 'None' pour les attributs qui ne nous interresse pas .
"""
def create_activitie_equipment(idEquipment, idActivity, nameActivity, levelActivity):
    #Je me connecte à ma base pour récupérer le(s) objet(s) en question.
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    listCondition = []

    # Je récupère les conditions pour la base de données, que j'insère ensuite dans la liste list_conditions
    if idEquipment != None :
        listCondition.append(" ID_EQUIPEMENTS = " + idEquipment)
    if idActivity != None :
        listCondition.append(" ID_ACTIVITES = " + idActivity)
    if nameActivity != None :
        listCondition.append(" NOM_ACTIVITES LIKE '%{}%'".format(nameActivity))
    if levelActivity != None :
        listCondition.append(" NIVEAU_ACTIVITE LIKE '%{}%'".format(levelActivity))
    # Je récupère ma requête à exécuter
    query = select_query('equipements_activites', listCondition)

    c.execute(query)

    list = []
    # Je parcours toute les lignes récupérées, et je crée pour chacune un objet
    for row in c :
        # Je créer mon objet puis je le stocke dans un dictionnaire avec pour clé le numéro d'activité
        obj = activities_equipments(row[0], row[1], row[2], row[3])
        list.append(obj)

    conn.close()
    return list
