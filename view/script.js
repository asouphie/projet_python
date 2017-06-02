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
