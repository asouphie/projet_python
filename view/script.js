var liste_filtre_ville;
var liste_filtre_activite;

function init() {
    var buttonAdd1 = document.getElementById('')
    var button = document.getElementById('buttonSearch');
    button.addEventListener("click", changerEcran, false);
}

function changerEcran() {
        document.getElementById('contenu').className = "cont";
        document.getElementById('map_google').className = "visible";
        document.getElementById('bandeau').className = "bandeau-action";
}

function addFiltre(select) {
    var valueSelect = document.getElementById(select).value;
    var zoneFiltre = document.getElementById('zone-filtre').innerHTML;

    if(valueSelect != '' && valueSelect != null) {
        zoneFiltre += '<a class="filtre" onClick="deleteFiltre()">'+valueSelect+'<img src="../view/delete.png" width="15"></a>';
        if(valueSelect == 'select_activites') {
            liste_filtre_activite.push(valueSelect);

        } else if (valueSelect == 'select_villes') {
            liste_filtre_ville.push(valueSelect);

        }
    }

    document.getElementById('zone-filtre').innerHTML = zoneFiltre;
    document.getElementById(select).value = "";
}

function deleteFiltre() {}

function reinitFiltre() {}

