$(document).ready(function(){

    $("#select_town").autocomplete({
        minLength : 3,
        source :
            function(requete, response) {
                //Je récupère la valeur de mon champs.
                var champs = $("#select_town").val();
                //Je vérifie si ce champs contient un nombre ou une string.
                var isNotChiffre = isNaN(champs);
                //datas correspond à ma string de paramètres que je rajouterais dans mon url pour la requête ajax.
                var datas = '';
                //Je créer ma string de paramètre en fonction de ma recherche.
                if(isNotChiffre) {
                    datas += "town="+champs;
                } else {
                    datas += "zip="+champs;
                }
                datas+="&max_rows=10";

                $.ajax({
                    url: '/list_town_zip',
                    type: 'GET',
                    data: datas,
                    dataType: 'json',
                    success:
                        //Lors de la récupération du JSON, si c'est un succes, je parcours la map datas
                        //et je retourne une string contenant la ville et son code postal.
                        function (datas) {
                            response($.map(datas, function (objet) {
                                return objet.town + " , " + objet.zip;
                            }));
                        },
                    error:
                        function (resultat, statut, erreur) {
                            alert('erreur');
                        },
                });
            },
        select : function () {
            //VOIR POUR STOCKER DANS UN INPUT HIDDEN LE CODE POSTAL
        }
    });

    $("#select_activities").autocomplete({
        minLength : 3,
        source :
            function(requete, response) {
                //Je récupère la valeur de mon champs.
                var champs = $("#select_activities").val();

                $.ajax({
                    url: '/list_activities',
                    type: 'GET',
                    data:
                        {
                            activity : champs,
                            max_rows : 10
                        },
                    dataType: 'json',
                    success:
                        //Lors de la récupération du JSON, si c'est un succes, je parcours la map datas
                        //et je retourne une string contenant le nom de l'activité.
                        function (datas) {
                            response($.map(datas, function (objet) {
                                return objet.name_activity;
                            }));
                        },
                    error:
                        function (resultat, statut, erreur) {
                            alert('erreur');
                        },
                });
            },
        select : function () {
            //DE MEME QUE PLUS HAUT POUR LES VILLES
        }
    });
});


