#!/usr/bin/env python
# -*- coding: utf-8 -*-

from objects.equipment import *
from objects.activities_equipments import *
from objects.installation import *

import codecs
import csv
import sqlite3


def create_table():
    """
        Fonction permettant de créer la base de données
    """

    # Connexion à la base de données
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()

    # On supprime les tables si elles sont déjà existante, pour éviter une erreur
    c.execute("DROP TABLE IF EXISTS installations")
    c.execute("DROP TABLE IF EXISTS equipement")
    c.execute("DROP TABLE IF EXISTS equipements_activites")

    # On ajoute les tables, avec les colonnes, les clés primaires et étrangères
    c.execute("CREATE TABLE installations ( NUMERO_INSTALLATON INT PRIMARY KEY NOT NULL,"\
                                            "NOM_INSTALLATIONS VARCHAR(255) NOT NULL,"\
                                            "NOM_COMMUNE VARCHAR(100),"\
                                            "CODE_POSTAL INT NOT NULL,"\
                                            "NUMERO_VOIE INT NOT NULL,"\
                                            "NOM_VOIE VARCHAR(255) NOT NULL)")

    c.execute("CREATE TABLE equipement ( ID_EQUIPEMENTS INT PRIMARY KEY NOT NULL,"\
                                        "NOM_EQUIPEMENTS VARCHAR(100) NOT NULL,"\
                                        "NUMERO_INSTALLATION INT NOT NULL,"\
                                        "EQUIGPSX VARCHAR(100) NOT NULL,"\
                                        "EQUIGPSY VARCHAR(100) NOT NULL)")

    c.execute("CREATE TABLE equipements_activites ( ID_ACTIVITES INT NOT NULL," \
                                                    "ID_EQUIPEMENTS INT NOT NULL,"\
                                                    "NOM_ACTIVITES VARCHAR(100) NOT NULL," \
                                                    "NIVEAU_ACTIVITE VARCHAR(100) NOT NULL)")

    # On commit les modifications sur la base puis on ferme la connexion.
    conn.commit()
    conn.close()


def add_datas():
    """
        Ajoute les valeurs des fichiers.csv dans la base de données créés en amont
    """

    # Connexion à la base, sauf si celle-ci n'existe pas, alors on l'a créer.
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()

    # Dans un premier temps, je récupère tous les fichiers .csv qui vont me servir à compléter ma base de données.
    file_equipment = codecs.open("files_csv/equipment.csv", "r", "utf-8")
    file_equipment_activities = codecs.open("files_csv/activities_equipments.csv", "r", "utf-8")
    file_installation = codecs.open("files_csv/installation.csv", "r", "utf-8")

    # Ensuite je le lis, pour pouvoir par la suite le parcourir ligne par ligne.
    # DictReader est une fonction permettant de retrouver une colonne via son nom et non son numéro.
    file_equipment = csv.DictReader(file_equipment)
    file_equipment_activities = csv.DictReader(file_equipment_activities)
    file_installation = csv.DictReader(file_installation)

    # Pour chaque fichier csv, je parcours chaque ligne et récupère les colonnes qui m'interesse pour ma base de donnée.
    for row in file_installation:
        obj_tmp = installation(row["Numéro de l'installation"], row["Nom usuel de l'installation"], row["Nom de la commune"],
                               row["Code postal"], row["Numero de la voie"], row["Nom de la voie"])
        obj_tmp.add_installation(c)

    for row in file_equipment:
        obj_tmp = equipment(row['EquipementId'], row['EquNom'], row['InsNumeroInstall'], row['EquGpsX'], row['EquGpsY'])
        obj_tmp.add_equipment(c)

    for row in file_equipment_activities:
        obj_tmp = activities_equipments(row['EquipementId'], row['ActCode'], row['ActLib'], row['ActNivLib'])
        obj_tmp.add_activities_equipments(c)

    conn.commit()
    conn.close()


create_table()
add_datas()
