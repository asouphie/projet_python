#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

""" Fonction généralisée permettant d'écrire les requêtes sql de SELECT avec les conditions """

def insert_query(table, list_conditions):
    insert_query = "SELECT * FROM " + table

    if len(list_conditions) == 1:
        insert_query = insert_query + " WHERE " + list_conditions[0]
        #return insert_query
    elif len(list_conditions) > 1:
        insert_query = insert_query + " WHERE "
        cpt = 0
        for condition in list_conditions:
            if len(list_conditions)-1 == cpt:
                insert_query = insert_query + condition
            else:
                insert_query = insert_query + condition + " AND "
            cpt += 1;

    return insert_query
