function init() {
    var button = document.getElementById('buttonSearch');
    button.addEventListener("click", changerEcran, false);
}

function changerEcran() {
        document.getElementById('contenu').className = "cont";
        document.getElementById('map_google').className = "visible";
        document.getElementById('bandeau').className = "bandeau-action";
}

function addFiltre(input) {
    var champInput = document.getElementById(input).value;
    var zoneFiltre = document.getElementById('zone-filtre').innerHTML;

    if(champInput != '' && champInput != null) {
        zoneFiltre += '<a class="filtre" onClick="deleteFiltre()">'+champInput+'<img src="../view/delete.png" width="15"></a>';
    }

    document.getElementById('zone-filtre').innerHTML = zoneFiltre;
    document.getElementById(input).value = "";
}

function deleteFiltre() {}

function reinitFiltre() {}

