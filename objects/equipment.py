#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datas.functions_datas import select_query

import sqlite3

class equipment :
    def __init__(self, ID_EQUIPEMENTS, NOM_EQUIPEMENTS, NUMERO_INSTALLATION, EQUIGPSX, EQUIGPSY):
        self.NUMERO_INSTALLATION = NUMERO_INSTALLATION
        self.ID_EQUIPEMENTS = ID_EQUIPEMENTS
        self.NOM_EQUIPEMENTS = NOM_EQUIPEMENTS
        self.EQUIGPSX = EQUIGPSX
        self.EQUIGPSY = EQUIGPSY

    def add_equipment(self, conn):
        """
            Permet d'ajouter un équipement dans la base de donnée
            :argument
                :parameter: conn correspond au cursor de la connexion en cours
        """
        insertQuery = "INSERT INTO equipement(ID_EQUIPEMENTS, NOM_EQUIPEMENTS, NUMERO_INSTALLATION, EQUIGPSX, EQUIGPSY) VALUES(?,?,?,?,?)"
        conn.execute(insertQuery, (self.ID_EQUIPEMENTS, self.NOM_EQUIPEMENTS, self.NUMERO_INSTALLATION, self.EQUIGPSX, self.EQUIGPSY))

def create_object_equipment(id_equipment, num_installation, name_equipment, equi_gps_x, equi_gps_y):
    """
        Permet, grâce à la base de données, de créer un ou des nouveaux objects équipements
        Pour filtrer les objects à récupérer, il suffit de mettre 'None' pour les attributs qui ne nous interresse pas
        :argument:
            :parameter: id_equipment
            :parameter: num_installation
            :parameter: name_equipment
            :parameter: equi_gps_x
            :parameter: equi_gps_y
    """

    #Je me connecte à ma base pour récupérer l'objet en question.
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    list_conditions = []

    # Je récupère les conditions pour la base de données, que j'insère ensuite dans la liste list_conditions
    if id_equipment != None :
        list_conditions.append(" ID_EQUIPEMENTS = " + id_equipment)
    if num_installation != None :
        list_conditions.append(" NUMERO_INSTALLATION = " + num_installation)
    if name_equipment != None :
        list_conditions.append(" NOM_EQUIPEMENTS LIKE " + name_equipment)
    if equi_gps_x != None :
        list_conditions.append("EQUIGPSX = " + equi_gps_x)
    if equi_gps_y != None :
        list_conditions.append("EQUIGPSY = " + equi_gps_y)
    # Je récupère ma requête à exécuter
    query = select_query('equipement', list_conditions)
    c.execute(query)

    list = []
    # Je parcours toute les lignes récupérées, et je crée pour chacune un objet
    for row in c :
        # Je créer mon objet puis je le stocke dans un dictionnaire avec pour clé le numéro d'équipement
        obj = equipment(row[0], row[1], row[2], row[3], row[4])
        list.append(obj)

    conn.close()
    return list