//On garde en mémoire la carte

//initialisation de la map pour la garder en mémoire
var map;
//initalisation du tableau qui contiendra tous les markers
var markers;

//initialisation d'une infowindow (affichage de plus d'info en cliquant sur la map)
var infowindow = null;

//Fonction appellée après avoir chargé l'API de google map
function initMap(){
	//On crée la carte qui sera dans le deuxième onglet
	var latlng = new google.maps.LatLng(47.1970673, -1.3611004);
	markers = []; // utilisé pour créer chaque marqueurs
  	map = new google.maps.Map(document.getElementById('map'), {
		zoom: 8,
		center: latlng,
		mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    //On initialise l'infowindow
    infowindow = new google.maps.InfoWindow({
		content: "holding..."
	});
}


$(document).ready(function(){

    $('#select_town').change(function() {
        var val = $('#select_town').val();
        var tmp = val.split(', ');
        $('#town').val(tmp[0]);
        $('#zip').val(tmp[1]);
    });

    $('#select_activities').change(function() {
        $('#activity').val("");
    });

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
                            response(datas);
                        },
                    error:
                        function (resultat, statut, erreur) {
                            alert('erreur');
                        },
                });
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
                            response(datas);
                        },
                    error:
                        function (resultat, statut, erreur) {
                            alert('erreur');
                        },
                });
            },
        select :
            function (event, data) {
                $("#activity").val(data.item.name_activity);
            }
    });

    $("#buttonSearch").on('click', function(){
        var datas = "";
        var activity = document.getElementById('activity').value;
        var town = document.getElementById('town').value;
        var zip = document.getElementById('zip').value;

        if(activity != "") {
            datas = "activity="+activity;
        }
        if(zip != "" && town != ""){
            if(datas.length > 0) {
                datas += "&";
            }
            datas += "town="+town+"&zip="+zip;
        }



        if(datas.length > 0) {
            $.ajax({
                url: '/search_activity',
                type: 'GET',
                data: datas,
                dataType: 'json',
                success:
                    function (datas) {
                        alert(datas);
                        var firstItem = true;
				        var mapCenter;

				        markers = new Array();

                        $.map(datas, function (objet) {
                            if (firstItem) {
                                mapCenter = new google.maps.LatLng(objet.latitude,objet.longitude)
                                map.panTo(mapCenter);
                                firstItem = false;
                            }

                            //marker à ajouter sur la carte
                            var marker = new google.maps.Marker({
                                position: new google.maps.LatLng(objet.latitude, objet.longitude),
                                map: map,
                                title: objet.towm + ": " + objet.name_act
                            })

                            var actLibInfoWindow = "<h3>" + objet.name_act + "(" + objet.niv_act + ")" + "</h3>";

                            google.maps.event.addListener(marker, 'click', function() {
                                //Contenu de l'infowindow
                                infowindow.setContent(actLibInfoWindow
                                                      + "<div>"
                                                      + objet.num_street+", "+objet.name_street
                                                      + "<br/>"
                                                      + objet.town+", "+objet.zip
                                                      + "</div>");
                                infowindow.open(map, this);
                            });

                            //J'ajoute un marqueur sur la carte
                            markers.push(marker);
                        });
                    },
                error:
                    function (resultat, statut, erreur) {
                        alert('erreur');
                    },
            });
        } else {
            alert("Veuillez renseigner une activité et/ou une ville.")
        }
    });
});


