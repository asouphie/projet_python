#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.activities_equipments import create_activitie_equipment
from classes.installation import create_installation, installation_for_activity

"""" Retourne une liste d'activités contenant l'id et le nom de l'activité. """
def list_activity(activity, maxRows):
    lstActivity = []
    lstIdActivity = []

    activities = create_activitie_equipment(None, None, activity, None)

    cpt = 0

    for activity in activities :
        if cpt <= int(maxRows) and activity.NOM_ACTIVITES not in lstIdActivity :
            cpt = cpt + 1
            lstIdActivity.append(activity.NOM_ACTIVITES)
            lstActivity.append({'label' : activity.NOM_ACTIVITES, 'value' : activity.NOM_ACTIVITES,
                                 'id_activity' : activity.ID_ACTIVITES, 'name_activity' : activity.NOM_ACTIVITES})
        elif cpt > int(maxRows) :
            break

    return lstActivity

""" Retourne une liste d'adresse contenant le code postale et le nom de la ville. """
def list_adress(town, zip, maxRows) :
    listTownZip = []
    listZip = []

    listInstallation = create_installation(None, None, town, zip, None, None, None, None, None, None, None, None)

    cpt = 0

    for installation in listInstallation :
        if cpt <= int(maxRows) and installation.CODE_POSTAL not in listZip :
            listZip.append(installation.CODE_POSTAL)
            str = "{}, {}".format(installation.NOM_COMMUNE,installation.CODE_POSTAL)
            listTownZip.append({'label' : str, 'value' : str,'zip' : installation.CODE_POSTAL, 'town' : installation.NOM_COMMUNE})
            cpt = cpt + 1
        elif cpt > int(maxRows) :
            break

    return listTownZip

def list_for_map(activity, zip, town):
    listForMap = installation_for_activity(zip, town, activity)
    return listForMap