<?php
$hostname = "localhost";
$usuario = "root";
$password = "Admin123";
$basededatos = "phpariketak";

$mysqli = new mysqli($hostname, $usuario, $password);

if (mysqli_connect_errno()) {
    echo "Error de conexión a la BD: " . mysqli_connect_error();
    exit();
}

$sql_db = "CREATE DATABASE IF NOT EXISTS $basededatos";
if ($mysqli->query($sql_db) === TRUE) {
    echo "Datu basea 'phpariketak' sortu da edo dagoeneko existitzen da.<br>";
} else {
    echo "Errorea datu basea sortzean: " . $mysqli->error . "<br>";
    exit();
}

$mysqli->select_db($basededatos);

$sql_table = "
CREATE TABLE IF NOT EXISTS Eraikuntza (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mota ENUM('Pisua', 'Txaleta', 'Etxea') NOT NULL,
    zonaldea ENUM('Alde zaharra', 'Deustu', 'Atxuri', 'Miribilla', 'Basurtu') NOT NULL,
    helbidea VARCHAR(100) NOT NULL,
    logelak ENUM('1', '2', '3', '4', '5') NOT NULL DEFAULT '3',
    prezioa DECIMAL(10,2) NOT NULL,
    tamaina DECIMAL(10,2) NOT NULL,
    extrak SET('Igerilekua', 'Lorategia', 'Garajea') DEFAULT NULL,
    irudia VARCHAR(50) DEFAULT NULL,
    oharrak TEXT DEFAULT NULL
)";
if ($mysqli->query($sql_table) === TRUE) {
    echo "Taula 'Eraikuntza' ongi sortu da edo dagoeneko existitzen da.<br>";
} else {
    echo "Errorea taula sortzean: " . $mysqli->error . "<br>";
}

$mysqli->close();
?>
