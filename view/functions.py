#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.activities_equipments import create_activitie_equipment
from classes.installation import create_installation

"""" Retourne une liste d'activités contenant l'id et le nom de l'activité. """
def list_activity(activity, max_rows):
    lst_activity = []
    lst_name_activity = []

    activities = create_activitie_equipment(None, None, activity, None)

    cpt = 0

    for activity in activities :
        name = activity.NOM_ACTIVITES.split("/")
        for name_activity in name :
            if cpt <= int(max_rows) and name_activity not in lst_name_activity :
                lst_name_activity.append(name_activity)
                lst_activity.append({"id_activity": activity.ID_ACTIVITES, "name_activity": name_activity})
            elif cpt > int(max_rows) :
                break
            else :
                continue

    return lst_activity

""" Retourne une liste d'adresse contenant le code postale et le nom de la ville. """
def list_adress(town, zip, max_rows) :
    list_town_zip = []
    list_zip = []

    list_installation = create_installation(None, None, town, zip, None, None, None, None, None, None, None, None)

    cpt = 0

    for installation in list_installation :
        if cpt <= int(max_rows) and installation.CODE_POSTAL not in list_zip :
            list_zip.append(installation.CODE_POSTAL)
            list_town_zip.append({"zip" : installation.CODE_POSTAL , "town" : installation.NOM_COMMUNE})
            cpt = cpt + 1
        elif cpt > int(max_rows) :
            break
        else :
            continue

    return list_town_zip