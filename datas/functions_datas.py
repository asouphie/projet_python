#!/usr/bin/env python
# -*- coding: utf-8 -*-

def select_query(table, list_conditions):
    """
        Fonction généralisée permettant d'écrire les requêtes sql de SELECT avec les conditions
    """
    query = "SELECT * FROM " + table

    #Si la liste de conditions est de longueur 1, ca signifie qu'on a une valeur simplement dans la première case du tableau
    #Donc pas besoin de faire de boucle sur list_conditions.
    if len(list_conditions) == 1:
        query = query + " WHERE " + list_conditions[0]
    #Sinon, on parcourt chaque valeur de la liste pour ensuite les rajouter à la chaine de caractères query, séparé de "AND".
    elif len(list_conditions) > 1:
        query = query + " WHERE "
        cpt = 0
        for condition in list_conditions:
            if len(list_conditions)-1 == cpt:
                query = query + condition
            else:
                query = query + condition + " AND "
            cpt += 1;

    return query