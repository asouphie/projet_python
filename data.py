#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import csv
import sqlite3

from classes.equipment import *
from classes.activities_equipments import *
from classes.installation import *

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
                                        "NUMERO_INSTALLATION INT NOT NULL,"\
                                        "CONSTRAINT fk_install FOREIGN KEY(NUMERO_INSTALLATION)"\
                                        "REFERENCES installation(NUMERO_INSTALLATION))")

    c.execute("CREATE TABLE equipements_activites ( ID_EQUIPEMENTS INT NOT NULL,"\
                                                    "ID_ACTIVITES INT NOT NULL," \
                                                    "NOM_ACTIVITES VARCHAR(100) NOT NULL," \
                                                    "NIVEAU_ACTIVITE VARCHAR(100) NOT NULL,"\
                                                    "CONSTRAINT fk_equipe FOREIGN KEY(ID_EQUIPEMENTS)"\
                                                    "REFERENCES equipement(ID_EQUIPEMENTS))")

    conn.commit()
    conn.close()


""" Ajoute les valeurs des fichiers.csv dans la base de données créés en amont """

def add_datas():
    # Connexion a database, if exist.
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()

    #Dans un premier temps, je récupère tous les fichiers .csv qui vont me servir à compléter ma base de données.
    file_equipment = codecs.open("files_csv/equipment.csv", "r", "utf-8")
    file_equipment_activities = codecs.open("files_csv/activities_equipments.csv", "r", "utf-8")
    file_installation = codecs.open("files_csv/installation.csv", "r", "utf-8")

    #Ensuite je le lis, pour pouvoir par la suite le parcourir ligne par ligne.
    #DictReader est une fonction permettant de retrouver une colonne via son nom et non son numéro.
    file_equipment = csv.DictReader(file_equipment)
    file_equipment_activities = csv.DictReader(file_equipment_activities)
    file_installation = csv.DictReader(file_installation)

    #Pour chaque fichier .csv, je parcours chaque ligne et récupère les colonnes qui m'interesse pour ma base de donnée.
    for row in file_equipment:
        obj_tmp = equipment(row['InsNumeroInstall'], row['EquipementId'], row['EquNom'])
        obj_tmp.add_equipment(c)

    for row in file_equipment_activities:
        obj_tmp = activities_equipments(row['EquipementId'], row['ActCode'], row['ActLib'], row['ActNivLib'])
        obj_tmp.add_activities_equipments(c)

    for row in file_installation:
        obj_tmp = installation(row["Numéro de l'installation"], row["Nom usuel de l'installation"], row["Nom de la commune"],
                               row["Code postal"], row["Nom du lieu dit"], row["Numero de la voie"], row["Nom de la voie"],
                               row['Longitude'], row['Latitude'], row["Aucun aménagement d'accessibilité"],
                               row['Accessibilité handicapés à mobilité réduite'], row['Accessibilité handicapés sensoriels'],
                               row['Nombre total de place de parking'], row['Nombre total de place de parking handicapés'],
                               row['Installation particulière'])
        obj_tmp.add_installation(c)

    conn.commit()
    conn.close()


def insert_query(table, list_conditions):
    insertQuery = "SELECT * FROM " + table

    if list_conditions.length == 0:
        return insertQuery
    elif list_conditions.length == 1:
        insertQuery = insertQuery + " WHERE " + list_conditions[0]
        return insertQuery
    elif list_conditions.length > 1:
        insertQuery = insertQuery + " WHERE "
        cpt = 0
        for condition in list_conditions:
            if list_conditions.length == cpt:
                insertQuery = insertQuery + list_conditions[cpt]
            else:
                insertQuery = insertQuery + list_conditions[cpt] + " AND "
            cpt += 1;
        return insertQuery

create_table()
add_datas()