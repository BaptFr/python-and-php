<?php
   $nombre1 = $_POST['nombre1'];
   # $nombre2 = 20;  
   $opérations = ["addition", "soustraction", "multiplication", "division"];
   $choix= "soustraction" ; 

   $resultat = 0;

    if($choix=="addition"){
        $resultat = $nombre1 + $nombre2;
        echo($resultat);
    }elseif($choix=="soustraction"){
        $resultat = $nombre1 - $nombre2;
        echo($resultat);
    }elseif($choix=="mutliplication"){
        $resultat = $nombre1 * $nombre2;
        echo($resultat);
    }else($choix=="division"){
        $resultat = $nombre1 / $nombre2;
        echo($resultat);
    }



?>
