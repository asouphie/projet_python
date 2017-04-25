<!DOCTYPE html>
<html >
    <head>
        <meta charset="UTF-8">
        <title>Sport Pays de la Loire</title>

        <link rel="stylesheet" href="../view/style.css">
    </head>

    <script type="text/javascript" src="../view/script.js"></script>

    <body onload="init()">
        <div id="contenu" class="cont cont-img">
            <div id ="bandeau" class="bandeau-connect">
                <div class="cont-bandeau">
                    <div class="logo-pdl">
                        <img src="../view/logo.png" height="353" width="958"/>
                    </div>
                    <div class="form-search">
                        <div class="champs-texte">
                            <input type="text" id="champVille" placeholder="Ville/Code Postal"/>
                            <a onclick="addFiltre('champVille')" class="logo-add">
                                <img src="../view/add.png" width="25">
                            </a>
                        </div>
                        <div class="champs-texte">
                            <input type="text" id="champActivite" placeholder="Activité"/>
                            <a onclick="addFiltre('champActivite');" class="logo-add">
                                <img src="../view/add.png" width="25">
                            </a>
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
