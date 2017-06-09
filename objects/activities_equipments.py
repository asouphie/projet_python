#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datas.functions_datas import select_query

import sqlite3

class activities_equipments :
    def __init__(self, ID_EQUIPEMENTS, ID_ACTIVITES, NOM_ACTIVITES, NIVEAU_ACTIVITE):
        self.ID_EQUIPEMENTS = ID_EQUIPEMENTS
        self.ID_ACTIVITES = ID_ACTIVITES
        self.NOM_ACTIVITES = NOM_ACTIVITES
        self.NIVEAU_ACTIVITE = NIVEAU_ACTIVITE

    def add_activities_equipments(self, conn):
        """
            Permet d'ajouter une activité dans la base de donnée
            :argument
                :parameter: conn correspond au cursor de la connexion en cours
        """
        insert_query = "INSERT INTO equipements_activites(ID_EQUIPEMENTS, ID_ACTIVITES, NOM_ACTIVITES, " \
                      "NIVEAU_ACTIVITE) VALUES(?,?,?,?)"
        conn.execute(insert_query, (self.ID_EQUIPEMENTS, self.ID_ACTIVITES, self.NOM_ACTIVITES, self.NIVEAU_ACTIVITE))


def create_object_activitie_equipment(id_equipment, id_activity, name_activity, level_activity):
    """
        Permet, grâce à la base de données, de créer un ou des nouveaux objects activités_equipements .
        Pour filtrer les objects à récupérer, il suffit de mettre 'None' pour les attributs qui ne nous interresse pas .
        :argument:
            :parameter: id_equipment
            :parameter: id_activity
            :parameter: name_activity
            :parameter: level_activity
    """

    #Je me connecte à ma base pour récupérer le(s) objet(s) en question.
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    list_condition = []

    # Je récupère les conditions pour la base de données, que j'insère ensuite dans la liste list_conditions
    if id_equipment != None :
        list_condition.append(" ID_EQUIPEMENTS = " + id_equipment)
    if id_activity != None :
        list_condition.append(" ID_ACTIVITES = " + id_activity)
    if name_activity != None :
        list_condition.append(" NOM_ACTIVITES LIKE '%{}%'".format(name_activity))
    if level_activity != None :
        list_condition.append(" NIVEAU_ACTIVITE LIKE '%{}%'".format(level_activity))
    # Je récupère ma requête à exécuter
    query = select_query('equipements_activites', list_condition)

    c.execute(query)

    list = []
    # Je parcours toute les lignes récupérées, et je crée pour chacune un objet
    for row in c :
        # Je créer mon objet puis je le stocke dans un dictionnaire avec pour clé le numéro d'activité
        obj = activities_equipments(row[0], row[1], row[2], row[3])
        list.append(obj)

    conn.close()
    return list
