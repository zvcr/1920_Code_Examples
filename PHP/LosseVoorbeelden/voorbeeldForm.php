<!DOCTYPE html>
<html>
<head>
    <title>Voorbeeld form</title>
</head>
<body>
    <form method="POST">
        Voornaam:<input type="text" name="txtVoornaam"/><br/>
        Achternaam:<input type="text" name="txtAchternaam"/><br/>
        <input type="submit" name="btnVerstuur"/>
    </form>
    <?php
    if(isset($_POST["btnVerstuur"])) {
        if(empty($_POST["txtVoornaam"])){
            echo "Er is geen voornaam ingevuld!<br/>";
        } else {
            echo "Voornaam: " . $_POST["txtVoornaam"] . "<br/>";
        }
        if(empty($_POST["txtAchternaam"])){
            echo "Er is geen achternaam ingevuld!";
        } else {
            echo "Achternaam: " . $_POST["txtAchternaam"];
        }
    }
    ?>
</body>
</html>