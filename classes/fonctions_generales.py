#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

""" Fonction généralisée permettant d'écrire les requêtes sql de SELECT avec les conditions """

def insert_query(table, list_conditions):
    insertQuery = "SELECT * FROM " + table

    #Si on n'as aucune condition de rentrer dans list_conditions, on retourne directement notre requête.
    if len(list_conditions) == 0:
        return insertQuery
    elif len(list_conditions) == 1:
        insertQuery = insertQuery + " WHERE " + list_conditions[0]
        return insertQuery
    elif len(list_conditions) > 1:
        insertQuery = insertQuery + " WHERE "
        cpt = 0
        for condition in list_conditions:
            if len(list_conditions)-1 == cpt:
                insertQuery = insertQuery + list_conditions[cpt]
            else:
                insertQuery = insertQuery + list_conditions[cpt] + " AND "
            cpt += 1;
    return insertQuery
