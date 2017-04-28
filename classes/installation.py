#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from data import insert_query

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


""" Permet, grâce à la base de données, de créer un ou des nouveaux objets installations """
#Pour filtrer les objets à récupérer, il suffit de mettre 'None' pour les attributs qui ne nous interresse pas

def create_activitie_equipment(id_installation, nom_installation, nom_commune, code_postal, lieu_dit, numero_voie, nom_voie,
                 longitude, latitude, aucun_amm_handi, acces_handi_reduit, acces_handi_sens):
    #Je me connecte à ma base pour récupérer l'objet en question.
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    list_conditions = []

    #Je récupère les conditions pour la base de données, que j'insère ensuite dans la liste list_conditions
    if id_installation != None :
        list_conditions.append(" NUMERO_INSTALLATON = " + id_installation)
    if nom_installation != None :
        list_conditions.append(" NUMERO_INSTALLATON LIKE " + nom_installation)
    if nom_commune != None :
        list_conditions.append(" NOM_COMMUNE LIKE " + nom_commune)
    if code_postal != None :
        list_conditions.append(" CODE_POSTAL = " + code_postal)
    if lieu_dit != None :
        list_conditions.append(" LIEU_DIT LIKE " + lieu_dit)
    if numero_voie != None :
        list_conditions.append(" NUMERO_VOIE = " + numero_voie)
    if nom_voie != None :
        list_conditions.append(" NOM_VOIE LIKE " + nom_voie)
    if longitude != None :
        list_conditions.append(" LONGITUDE = " + longitude)
    if latitude != None :
        list_conditions.append(" LATITUDE = " + latitude)
    if aucun_amm_handi != None :
        list_conditions.append(" AUCUN_AMENAGEMENT_ACCESSIBILITE = " + aucun_amm_handi)
    if acces_handi_reduit != None :
        list_conditions.append(" ACCESSIBILITE_HANDICAPE_MOBILITE_REDUITE = " + acces_handi_reduit)
    if acces_handi_sens != None :
        list_conditions.append(" ACCESSIBILITE_HANDICAPE_SENSORIEL = " + acces_handi_sens)
    #Je récupère ma requête à exécuter
    insertQuery = insert_query('installations', list_conditions)

    c.execute(insertQuery)

    d = {}
    #Je parcours toute les lignes récupérées, et je crée pour chacune un objet
    for row in c :
        #Je créer mon objet puis je le stocke dans un dictionnaire avec pour clé le numéro d'installation
        obj = installation(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14])
        d = {row[0]:obj}

    conn.close()
    return d