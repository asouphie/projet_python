#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Fonction généralisée permettant d'écrire les requêtes sql de SELECT avec les conditions """
def select_query(table, listConditions):
    query = "SELECT * FROM " + table

    if len(listConditions) == 1:
        query = query + " WHERE " + listConditions[0]
        #return insert_query
    elif len(listConditions) > 1:
        query = query + " WHERE "
        cpt = 0
        for condition in listConditions:
            if len(listConditions)-1 == cpt:
                query = query + condition
            else:
                query = query + condition + " AND "
            cpt += 1;

    return query
