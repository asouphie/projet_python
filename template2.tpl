<!DOCTYPE html>
<html >
    <head>
        <meta charset="UTF-8">
        <title>Sport Pays de la Loire</title>

        <link rel="stylesheet" href="../view/style.css">
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/jquery-ui.min.js"></script>
        <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/themes/smoothness/jquery-ui.css" />
        <script type="text/javascript" src="../view/script.js"></script>
        <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyASAVFs7bKA1IoXiTDoz2IOE5dD7fzGx4g&callback=initMap"></script>

    </head>

    <body>

    <input type="hidden" id="zip" value="">
    <input type="hidden" id="town" value="">
    <input type="hidden" id="activity" value="">

        <div id="contenu" class="cont">
            <div id="map"></div>
            <div id ="bandeau" class="bandeau-action">
                <div class="cont-bandeau">
                    <div class="logo-pdl">
                        <img src="../view/logo.png" height="353" width="958"/>
                    </div>
                    <div class="form-search">
                        <div class="champs-texte">
                            <input type="text" id="select_town" placeholder="Ville/Code Postal"/>
                        </div>
                        <div class="champs-texte">
                            <input type="text" id="select_activities" placeholder="Activité"/>
                        </div>
                        <button id="buttonSearch" type="button">Rechercher</button>
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>
