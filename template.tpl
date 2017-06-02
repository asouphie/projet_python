<!DOCTYPE html>
<html >
    <head>
        <meta charset="UTF-8">
        <title>Sport Pays de la Loire</title>

        <link rel="stylesheet" href="../view/style.css">
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
        <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/themes/smoothness/jquery-ui.css" />
        <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/jquery-ui.min.js"></script>
        <script type="text/javascript" src="../view/script.js"></script>
        <script type="text/javascript" src="../view/jquery.js"></script>
    </head>

    <body onload="init()">

        <div id="contenu" class="cont cont-img">
            <div id ="bandeau" class="bandeau-connect">
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
                        <div id="zone-filtre"></div>
                        <button id="buttonSearch" type="button">Rechercher</button>
                    </div>
                </div>
            </div>
            <!-- Maps Google -->
            <div id="map_google" class="invisible">
                <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d10836.628492593924!2d-1.5506799500000001!3d47.233072400000005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sfr!2sfr!4v1490942904128" width="1500" height="1500" frameborder="0" style="border:0" allowfullscreen></iframe>
            </div>
        </div>
    </body>
</html>
