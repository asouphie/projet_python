#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from data import insert_query

class equipment :
    def __init__(self, NUMERO_INSTALLATION, ID_EQUIPEMENTS, NOM_EQUIPEMENTS ):
        self.NUMERO_INSTALLATION = NUMERO_INSTALLATION
        self.ID_EQUIPEMENTS = ID_EQUIPEMENTS
        self.NOM_EQUIPEMENTS = NOM_EQUIPEMENTS

    """ Permet d'ajouter un équipement dans la base de donnée """

    def add_equipment(self, conn):
        insertQuery = "INSERT INTO equipement(NUMERO_INSTALLATION, ID_EQUIPEMENTS, NOM_EQUIPEMENTS) VALUES(?,?,?)"
        conn.execute(insertQuery, (self.NUMERO_INSTALLATION, self.ID_EQUIPEMENTS, self.NOM_EQUIPEMENTS))


""" Permet, grâce à la base de données, de créer un ou des nouveaux objets équipements """
#Pour filtrer les objets à récupérer, il suffit de mettre 'None' pour les attributs qui ne nous interresse pas

def create_equipment(id_equipment, numero_installation, nom_equipement):
    #Je me connecte à ma base pour récupérer l'objet en question.
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    list_conditions = []

    # Je récupère les conditions pour la base de données, que j'insère ensuite dans la liste list_conditions
    if id_equipment != None :
        list_conditions.append(" ID_EQUIPEMENTS = " + id_equipment)
    if numero_installation != None :
        list_conditions.append(" NUMERO_INSTALLATION = " + numero_installation)
    if nom_equipement != None :
        list_conditions.append(" NOM_EQUIPEMENTS LIKE " + nom_equipement)
    # Je récupère ma requête à exécuter
    insertQuery = insert_query('equipement', list_conditions)

    c.execute(insertQuery)

    d = {}
    # Je parcours toute les lignes récupérées, et je crée pour chacune un objet
    for row in c :
        # Je créer mon objet puis je le stocke dans un dictionnaire avec pour clé le numéro d'équipement
        obj = equipment(row[0], row[1], row[2])
        d = {row[1]:obj}

    conn.close()
    return d