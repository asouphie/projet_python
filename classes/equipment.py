#!/usr/bin/env python
# -*- coding: utf-8 -*-

class equipment :
    def __init__(self, NUMERO_INSTALLATION, ID_EQUIPEMENTS, NOM_EQUIPEMENTS ):
        self.NUMERO_INSTALLATION = NUMERO_INSTALLATION
        self.ID_EQUIPEMENTS = ID_EQUIPEMENTS
        self.NOM_EQUIPEMENTS = NOM_EQUIPEMENTS

    """ Permet d'ajouter un équipement dans la base de donnée """

    def add_equipment(self, conn):
        insertQuery = "INSERT INTO equipement(NUMERO_INSTALLATION, ID_EQUIPEMENTS, NOM_EQUIPEMENTS) VALUES(?,?,?)"
        conn.execute(insertQuery, (self.NUMERO_INSTALLATION, self.ID_EQUIPEMENTS, self.NOM_EQUIPEMENTS))