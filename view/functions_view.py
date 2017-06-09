#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

from objects.activities_equipments import create_object_activitie_equipment
from objects.installation import create_object_installation

def list_activity(activity, max_rows):
    """"
        Retourne une liste d'activités contenant l'id et le nom de l'activité.
        :argument:
            :parameter: activity
            :parameter: max_rows
    """

    lst_activity = []
    lst_id_activity = []

    #Je récupère dans la base de données les activités dont le nom est similaire à activity.
    activities = create_object_activitie_equipment(None, None, activity, None)

    cpt = 0

    #Pour chaque activité récupérée, je vérifie si son nom n'est pas déjà présent
    #Si ce n'est pas le cas, alors j'ajoute à la liste que je retourne un objet que je créer avec
    #un label, une value, un id_activity et une name_activity. Cet objet me servira dans l'auto-complete du site.
    for activity in activities :
        if cpt <= int(max_rows) and activity.NOM_ACTIVITES not in lst_id_activity :
            cpt = cpt + 1
            lst_id_activity.append(activity.NOM_ACTIVITES)
            lst_activity.append({'label' : activity.NOM_ACTIVITES, 'value' : activity.NOM_ACTIVITES,
                                 'id_activity' : activity.ID_ACTIVITES, 'name_activity' : activity.NOM_ACTIVITES})
        elif cpt > int(max_rows) :
            break

    return lst_activity

def list_adress(town, zip, max_rows) :
    """
        Retourne une liste d'adresse contenant le code postale et le nom de la ville.
        :argument:
            :parameter: town
            :parameter: zip
            :parameter: max_rows
    """
    list_town_zip = []
    list_zip = []

    # Je récupère dans la base de données les installations dont la ville et le code postal sont similaires à zip ou town.
    list_installation = create_object_installation(None, None, town, zip, None, None)

    cpt = 0

    #Pour chaque installation récupérée, je vérifie si son code postal n'est pas déjà présent
    #Si ce n'est pas le cas, alors j'ajoute à la liste que je retourne un objet que je créer avec
    #un label, une value, un code_postal et une ville. Cet objet me servira dans l'auto-complete du site.
    for installation in list_installation :
        if cpt <= int(max_rows) and installation.CODE_POSTAL not in list_zip :
            list_zip.append(installation.CODE_POSTAL)
            str = "{}, {}".format(installation.NOM_COMMUNE,installation.CODE_POSTAL)
            list_town_zip.append({'label' : str, 'value' : str,'zip' : installation.CODE_POSTAL, 'town' : installation.NOM_COMMUNE})
            cpt = cpt + 1
        elif cpt > int(max_rows) :
            break

    return list_town_zip

def list_for_map(activity, zip, town):
    """
        Retourne une liste d'objet qui contient toute les informations nécessaires pour les markers de la google map.
        :argument:
            :parameter: activity
            :parameter: zip
            :parameter: town
    """
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()

    query = "SELECT DISTINCT i.NOM_INSTALLATIONS, i.NUMERO_VOIE, i.NOM_VOIE, i.NOM_COMMUNE, i.CODE_POSTAL, " \
            "a.NOM_ACTIVITES, a.NIVEAU_ACTIVITE, e.NOM_EQUIPEMENTS, e.EQUIGPSX, e.EQUIGPSY  " \
            "FROM equipement AS e INNER JOIN equipements_activites AS a ON"

    if activity != None:
        query = query + " a.NOM_ACTIVITES = '{}' AND".format(activity)

    query = query + " e.ID_EQUIPEMENTS = a.ID_EQUIPEMENTS INNER JOIN installations AS i ON e.NUMERO_INSTALLATION = i.NUMERO_INSTALLATON"

    if zip != None and town != None:
        query = query + " AND i.NOM_COMMUNE = '{}' AND i.CODE_POSTAL = '{}'".format(town, zip)

    c.execute(query)

    list = []

    for row in c:
        list.append(
            {'name_install': row[0], 'num_street': row[1], 'name_street': row[2], 'town': row[3], 'zip': row[4],
             'name_act': row[5], 'niv_act': row[6], 'name_equipment': row[7], 'equi_gps_x': row[8],
             'equi_gps_y': row[9]})

    conn.commit()
    conn.close()

    return list