<?php
$hostname = "localhost";
$usuario = "root";
$password = "Admin123";
$basededatos = "phpariketak";

$mysqli = new mysqli($hostname, $usuario, $password, $basededatos);

if ($mysqli->connect_error) {
    die("Errorea konexioan: " . $mysqli->connect_error);
}

if (isset($_POST['delete_ids']) && is_array($_POST['delete_ids'])) {
    $ids_to_delete = $_POST['delete_ids'];
    $ids_to_delete = implode(",", $ids_to_delete);

    $query = "DELETE FROM Eraikuntza WHERE id IN ($ids_to_delete)";
    
    if ($mysqli->query($query)) {
        echo "Etxebizitzak ongi ezabatuta.<br>";
    } else {
        echo "Errorea etxebizitzak ezabatzean: " . $mysqli->error . "<br>";
    }
} else {
    echo "Ez dago etxebizitza aukeraturik ezabatzeko.<br>";
}

$mysqli->close();

header("Location: index.php");
exit();
?>
