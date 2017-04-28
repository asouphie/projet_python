#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from data import insert_query

class activities_equipments :
    def __init__(self, ID_EQUIPEMENTS, ID_ACTIVITES, NOM_ACTIVITES, NIVEAU_ACTIVITE):
        self.ID_EQUIPEMENTS = ID_EQUIPEMENTS
        self.ID_ACTIVITES = ID_ACTIVITES
        self.NOM_ACTIVITES = NOM_ACTIVITES
        self.NIVEAU_ACTIVITE = NIVEAU_ACTIVITE

    """ Permet d'ajouter une activité dans la base de donnée"""

    def add_activities_equipments(self, conn):
        insertQuery = "INSERT INTO equipements_activites(ID_EQUIPEMENTS, ID_ACTIVITES, NOM_ACTIVITES, " \
                      "NIVEAU_ACTIVITE) VALUES(?,?,?,?)"
        conn.execute(insertQuery, (self.ID_EQUIPEMENTS, self.ID_ACTIVITES,
                                   self.NOM_ACTIVITES, self.NIVEAU_ACTIVITE))

    def create_activitie_equipment(conn, id_equipment):
        insertQuery = "SELECT * FROM equipements_activites WHERE ID_EQUIPEMENTS = ?"
        c = conn.cursor()
        c.execute(insertQuery, id_equipment);

        for row in c :
            print(row)


""" Permet, grâce à la base de données, de créer un ou des nouveaux objets activités_equipements """
#Pour filtrer les objets à récupérer, il suffit de mettre 'None' pour les attributs qui ne nous interresse pas

def create_activitie_equipment(id_equipment, id_activite, nom_activite, niveau_activite):
    #Je me connecte à ma base pour récupérer le(s) objet(s) en question.
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    list_condition = []

    # Je récupère les conditions pour la base de données, que j'insère ensuite dans la liste list_conditions
    if id_equipment != None :
        list_condition.append(" ID_EQUIPEMENTS = " + id_equipment)
    if id_activite != None :
        list_condition.append(" ID_ACTIVITES = " + id_equipment)
    if nom_activite != None :
        list_condition.append(" NOM_ACTIVITES LIKE " + nom_activite)
    if niveau_activite != None :
        list_condition.append(" NIVEAU_ACTIVITE LIKE " + niveau_activite)
    # Je récupère ma requête à exécuter
    insertQuery = insert_query('equipements_activites', list_condition)

    c.execute(insertQuery)

    d = {}
    # Je parcours toute les lignes récupérées, et je crée pour chacune un objet
    for row in c :
        # Je créer mon objet puis je le stocke dans un dictionnaire avec pour clé le numéro d'activité
        obj = activities_equipments(row[0], row[1], row[2], row[3])
        d = {row[1]:obj}

    conn.close()
    return d
