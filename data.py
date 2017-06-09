#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.equipment import *
from classes.activities_equipments import *
from classes.installation import *

import codecs
import csv
import sqlite3

""" Fonction permettant de créer la base de données """
def create_table():
    #Connexion à la base de données
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()

    #On supprime les tables si elles sont déjà existante, pour éviter une erreur
    c.execute("DROP TABLE IF EXISTS installations")
    c.execute("DROP TABLE IF EXISTS equipement")
    c.execute("DROP TABLE IF EXISTS equipements_activites")

    #On ajoute les tables, avec les colonnes, les clés primaires et étrangères
    c.execute("CREATE TABLE installations ( NUMERO_INSTALLATON INT PRIMARY KEY NOT NULL,"\
                                            "NOM_INSTALLATIONS VARCHAR(255) NOT NULL,"\
                                            "NOM_COMMUNE VARCHAR(100),"\
                                            "CODE_POSTAL INT NOT NULL,"\
                                            "LIEU_DIT VARCHAR(255),"\
                                            "NUMERO_VOIE INT NOT NULL,"\
                                            "NOM_VOIE VARCHAR(255) NOT NULL,"\
                                            "LONGITUDE VARCHAR(100) NOT NULL,"\
                                            "LATITUDE VARCHAR(100) NOT NULL,"\
                                            "AUCUN_AMENAGEMENT_ACCESSIBILITE VARCHAR(3),"\
                                            "ACCESSIBILITE_HANDICAPE_MOBILITE_REDUITE VARCHAR(3) NOT NULL,"\
                                            "ACCESSIBILITE_HANDICAPE_SENSORIEL VARCHAR(3) NOT NULL,"\
                                            "PLACE_PARKING INT,"\
                                            "PLACE_PARKING_HANDICAPE INT,"\
                                            "INSTALLATION_PARTICULIERE VARCHAR(255))")

    c.execute("CREATE TABLE equipement ( ID_EQUIPEMENTS INT PRIMARY KEY NOT NULL,"\
                                        "NOM_EQUIPEMENTS VARCHAR(100) NOT NULL,"\
                                        "NUMERO_INSTALLATION INT NOT NULL)")

    c.execute("CREATE TABLE equipements_activites ( ID_ACTIVITES INT NOT NULL," \
                                                    "ID_EQUIPEMENTS INT NOT NULL,"\
                                                    "NOM_ACTIVITES VARCHAR(100) NOT NULL," \
                                                    "NIVEAU_ACTIVITE VARCHAR(100) NOT NULL)")

    conn.commit()
    conn.close()


""" Ajoute les valeurs des fichiers.csv dans la base de données créés en amont """
def add_datas():
    # Connexion a database, if exist.
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()

    #Dans un premier temps, je récupère tous les fichiers .csv qui vont me servir à compléter ma base de données.
    fileEquipment = codecs.open("files_csv/equipment.csv", "r", "utf-8")
    fileEquipmentActivities = codecs.open("files_csv/activities_equipments.csv", "r", "utf-8")
    fileInstallation = codecs.open("files_csv/installation.csv", "r", "utf-8")

    #Ensuite je le lis, pour pouvoir par la suite le parcourir ligne par ligne.
    #DictReader est une fonction permettant de retrouver une colonne via son nom et non son numéro.
    fileEquipment = csv.DictReader(fileEquipment)
    fileEquipmentActivities = csv.DictReader(fileEquipmentActivities)
    fileInstallation = csv.DictReader(fileInstallation)

    #Pour chaque fichier .csv, je parcours chaque ligne et récupère les colonnes qui m'interesse pour ma base de donnée.
    for row in fileInstallation:
        obj_tmp = installation(row["Numéro de l'installation"], row["Nom usuel de l'installation"], row["Nom de la commune"],
                               row["Code postal"], row["Nom du lieu dit"], row["Numero de la voie"], row["Nom de la voie"],
                               row['Longitude'], row['Latitude'], row["Aucun aménagement d'accessibilité"],
                               row['Accessibilité handicapés à mobilité réduite'], row['Accessibilité handicapés sensoriels'],
                               row['Nombre total de place de parking'], row['Nombre total de place de parking handicapés'],
                               row['Installation particulière'])
        obj_tmp.add_installation(c)

    for row in fileEquipment:
        obj_tmp = equipment(row['EquipementId'], row['EquNom'], row['InsNumeroInstall'])
        obj_tmp.add_equipment(c)


    for row in fileEquipmentActivities:
        obj_tmp = activities_equipments(row['EquipementId'], row['ActCode'], row['ActLib'], row['ActNivLib'])
        obj_tmp.add_activities_equipments(c)


    conn.commit()
    conn.close()

create_table()
add_datas()