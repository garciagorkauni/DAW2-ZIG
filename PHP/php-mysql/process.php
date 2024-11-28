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

$query = "SELECT mota, zonaldea, helbidea, logelak, prezioa, tamaina, extrak, irudia FROM Eraikuntza ORDER BY prezioa ASC";
$result = $mysqli->query($query);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($row['mota']) . "</td>";
        echo "<td>" . htmlspecialchars($row['zonaldea']) . "</td>";
        echo "<td>" . htmlspecialchars($row['helbidea']) . "</td>";
        echo "<td>" . htmlspecialchars($row['logelak']) . "</td>";
        echo "<td>" . htmlspecialchars($row['prezioa']) . " €</td>";
        echo "<td>" . htmlspecialchars($row['tamaina']) . " m²</td>";
        echo "<td>" . htmlspecialchars($row['extrak']) . "</td>";
        echo "<td>
                <a href='images/" . htmlspecialchars($row['irudia']) . "' target='_blank'>" 
                . htmlspecialchars($row['irudia']) . 
                "</a>
            </td>";
        echo "</tr>";
    }
} else {
    echo "<tr><td colspan='8'>Ez dago daturik</td></tr>";
}

$mysqli->close();
?>
