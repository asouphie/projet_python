class activities_equipments :
    def __init__(self, ID_EQUIPEMENTS, ID_ACTIVITES, NOM_ACTIVITES, NIVEAU_ACTIVITE):
        self.ID_EQUIPEMENTS = ID_EQUIPEMENTS
        self.ID_ACTIVITES = ID_ACTIVITES
        self.NOM_ACTIVITES = NOM_ACTIVITES
        self.NIVEAU_ACTIVITE = NIVEAU_ACTIVITE

    """ Permet d'ajouter une activité dans la base de donnée"""

    def add_activities_equipments(self, conn):
        insertQuery = "INSERT INTO equipements_activites(ID_EQUIPEMENTS, ID_ACTIVITES, NOM_ACTIVITES, " \
                      "NIVEAU_ACTIVITE) VALUES(?,?,?,?)"
        conn.execute(insertQuery, (self.ID_EQUIPEMENTS, self.ID_ACTIVITES,
                                   self.NOM_ACTIVITES, self.NIVEAU_ACTIVITE))