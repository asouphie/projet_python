$(document).ready(function(){
    $("#select_villes").autocomplete({
        source : JSON.parse("["+document.getElementById('list_ville_cp').value+"]"),
        select : function () {
            $('#img_ville').attr("src","../view/add.png");
        }
    });

    $("#select_activites").autocomplete({
        source : JSON.parse("["+document.getElementById('list_activite').value+"]"),
        select : function () {
            $('#img_activite').attr("src","../view/add.png");
        }
    });
});


