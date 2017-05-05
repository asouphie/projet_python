#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.activities_equipments import create_activitie_equipment
from classes.installation import create_installation

"""" Retourne une string contenant toute les activités, séparées par des virgules, pour la stocker par la suite dans un input. """

def list_activite() :
    list_act = ""
    premier = True

    list_act_equi = create_activitie_equipment(None, None, None, None)

    for act_equi in list_act_equi :
        nom = act_equi.NOM_ACTIVITES.split("/")
        for name in nom :
            if premier :
                list_act = '"'+ name + '"'
                premier = False
            elif name not in list_act:
                list_act = list_act + ', "' + name + '"'

    return list_act

""" Retourne un dictionnaire contenant comme clé le code postale et comme valeur le nom de la ville. """

def dico_ville() :
    dico_ville_cp = {}

    list_installations = create_installation(None, None, None, None, None, None, None, None, None, None, None, None)

    for installation in list_installations :
        if installation.NOM_COMMUNE not in dico_ville_cp.values() :
            dico_ville_cp[installation.CODE_POSTAL] = installation.NOM_COMMUNE

    return dico_ville_cp

""" Retourne une string contenant tous les noms des villes, sans les doublons, séparées par une virgule. """

def list_ville() :
    list_ville_cp = dico_ville()
    list_villes = ""

    premier = True;

    for ville in list_ville_cp.values() :
        if premier :
            list_villes = '"' + ville + '"'
            premier = False
        elif ville not in list_villes :
            list_villes = list_villes + ', "' + ville + '"'

    return list_villes

"""" Retourne une string contenant tous les codes postales, sans les doublons, séparées par une virgule. """

def list_cp() :
    list_ville_cp = dico_ville()
    list_cps = ""

    premier = True;

    for cp in list_ville_cp :
        if premier :
            list_cps = '"' + str(cp) + '"'
            premier = False
        elif str(cp) not in list_cps :
            list_cps = list_cps + ', "' + str(cp) + '"'

    return list_cps