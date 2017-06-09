#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.fonctions_generales import select_query

import sqlite3

class installation :
    def __init__(self, NUMERO_INSTALLATON, NOM_INSTALLATIONS, NOM_COMMUNE, CODE_POSTAL, LIEU_DIT, NUMERO_VOIE, NOM_VOIE,
                 LONGITUDE, LATITUDE, AUCUN_AMENAGEMENT_ACCESSIBILITE, ACCESSIBILITE_HANDICAPE_MOBILITE_REDUITE,
                 ACCESSIBILITE_HANDICAPE_SENSORIEL, PLACE_PARKING, PLACE_PARKING_HANDICAPE, INSTALLATION_PARTICULIERE):

        self.NOM_INSTALLATIONS = NOM_INSTALLATIONS
        self.NUMERO_INSTALLATON = NUMERO_INSTALLATON
        self.CODE_POSTAL = CODE_POSTAL
        self.LIEU_DIT = LIEU_DIT
        self.NUMERO_VOIE = NUMERO_VOIE
        self.NOM_VOIE = NOM_VOIE
        self.NOM_COMMUNE = NOM_COMMUNE
        self.LONGITUDE = LONGITUDE
        self.LATITUDE = LATITUDE
        self.AUCUN_AMENAGEMENT_ACCESSIBILITE = AUCUN_AMENAGEMENT_ACCESSIBILITE
        self.ACCESSIBILITE_HANDICAPE_MOBILITE_REDUITE = ACCESSIBILITE_HANDICAPE_MOBILITE_REDUITE
        self.ACCESSIBILITE_HANDICAPE_SENSORIEL = ACCESSIBILITE_HANDICAPE_SENSORIEL
        self.PLACE_PARKING = PLACE_PARKING
        self.PLACE_PARKING_HANDICAPE = PLACE_PARKING_HANDICAPE
        self.INSTALLATION_PARTICULIERE = INSTALLATION_PARTICULIERE

    """ Permet d'ajouter une installation dans la base de donnée """
    def add_installation(self, conn):
        insertQuery = "INSERT INTO installations(NUMERO_INSTALLATON, NOM_INSTALLATIONS, NOM_COMMUNE, CODE_POSTAL, LIEU_DIT, NUMERO_VOIE, NOM_VOIE,\
                                                    LONGITUDE, LATITUDE, AUCUN_AMENAGEMENT_ACCESSIBILITE, ACCESSIBILITE_HANDICAPE_MOBILITE_REDUITE,\
                                                    ACCESSIBILITE_HANDICAPE_SENSORIEL, PLACE_PARKING, PLACE_PARKING_HANDICAPE, INSTALLATION_PARTICULIERE)\
                                                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        conn.execute(insertQuery, ( self.NUMERO_INSTALLATON, self.NOM_INSTALLATIONS, self.NOM_COMMUNE, self.CODE_POSTAL, self.LIEU_DIT, self.NUMERO_VOIE,
                                    self.NOM_VOIE, self.LONGITUDE, self.LATITUDE, self.AUCUN_AMENAGEMENT_ACCESSIBILITE, self.ACCESSIBILITE_HANDICAPE_MOBILITE_REDUITE,
                                    self.ACCESSIBILITE_HANDICAPE_SENSORIEL, self.PLACE_PARKING, self.PLACE_PARKING_HANDICAPE, self.INSTALLATION_PARTICULIERE ))


"""
    Permet, grâce à la base de données, de créer un ou des nouveaux objets installations
    Pour filtrer les objets à récupérer, il suffit de mettre 'None' pour les attributs qui ne nous interresse pas
"""
def create_installation(idInstallation, nameInstallation, town, zip, lieuDit, numStreet, nameStreet,
                 longitude, latitude, aucun_amm_handi, acces_handi_reduit, acces_handi_sens):
    #Je me connecte à ma base pour récupérer l'objet en question.
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    listConditions = []

    #Je récupère les conditions pour la base de données, que j'insère ensuite dans la liste list_conditions
    if idInstallation != None :
        listConditions.append(" NUMERO_INSTALLATON = " + idInstallation)
    if nameInstallation != None :
        listConditions.append(" NOM_INSTALLATIONS LIKE '%{}%'".format(nameInstallation))
    if town != None :
        listConditions.append(" NOM_COMMUNE LIKE '%{}%'".format(town))
    if zip != None :
        listConditions.append(" CODE_POSTAL LIKE '%{}%'".format(zip))
    if lieuDit != None :
        listConditions.append(" LIEU_DIT LIKE '%{}%'".format(lieuDit))
    if numStreet != None :
        listConditions.append(" NUMERO_VOIE = " + numStreet)
    if nameStreet != None :
        listConditions.append(" NOM_VOIE LIKE '%{}%'".format(nameStreet))
    if longitude != None :
        listConditions.append(" LONGITUDE = " + longitude)
    if latitude != None :
        listConditions.append(" LATITUDE = " + latitude)
    if aucun_amm_handi != None :
        listConditions.append(" AUCUN_AMENAGEMENT_ACCESSIBILITE = " + aucun_amm_handi)
    if acces_handi_reduit != None :
        listConditions.append(" ACCESSIBILITE_HANDICAPE_MOBILITE_REDUITE = " + acces_handi_reduit)
    if acces_handi_sens != None :
        listConditions.append(" ACCESSIBILITE_HANDICAPE_SENSORIEL = " + acces_handi_sens)

    #Je récupère ma requête à exécuter
    query = select_query('installations', listConditions)
    c.execute(query)

    list = []
    #Je parcours toute les lignes récupérées, et je crée pour chacune un objet
    for row in c :
        #Je créer mon objet puis je le stocke dans un dictionnaire avec pour clé le numéro d'installation
        obj = installation(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14])
        list.append(obj)

    conn.close()
    return list

"""
    Permet de retourner une liste d'objet contenant tout ce que je souhaite utiliser pour les
    :argument
        :parameter: zip

"""
def installation_for_activity(zip, town, nameActivity) :
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()

    query = "SELECT DISTINCT i.NOM_INSTALLATIONS, i.NUMERO_VOIE, i.NOM_VOIE, i.NOM_COMMUNE, i.CODE_POSTAL, i.LONGITUDE, i.LATITUDE," \
                   "a.NOM_ACTIVITES, a.NIVEAU_ACTIVITE, e.NOM_EQUIPEMENTS  FROM equipement AS e INNER JOIN equipements_activites AS a ON"

    if nameActivity != None :
        query = query + " a.NOM_ACTIVITES = '{}' AND".format(nameActivity)

    query = query + " e.ID_EQUIPEMENTS = a.ID_EQUIPEMENTS INNER JOIN installations AS i ON e.NUMERO_INSTALLATION = i.NUMERO_INSTALLATON"

    if zip != None and town != None :
        query = query + " AND i.NOM_COMMUNE = '{}' AND i.CODE_POSTAL = '{}'".format(town, zip)


    c.execute(query)

    list = []

    for row in c :
        list.append({'name_install' : row[0], 'num_street' : row[1], 'name_street' : row[2], 'town' : row[3], 'zip' : row[4],
                     'longitude': row[5], 'latitude': row[6], 'name_act' : row[7], 'niv_act' : row[8], 'name_equipment' : row[9]})

    conn.commit()
    conn.close()

    return list

