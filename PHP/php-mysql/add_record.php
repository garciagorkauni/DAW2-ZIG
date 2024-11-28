<?php
$hostname = "localhost";
$usuario = "root";
$password = "Admin123";
$basededatos = "phpariketak";

$mysqli = new mysqli($hostname, $usuario, $password, $basededatos);

if ($mysqli->connect_error) {
    die("Errorea konexioan: " . $mysqli->connect_error);
}

$mota = $_POST['mota'];
$zonaldea = $_POST['zonaldea'];
$helbidea = $_POST['helbidea'];
$logelak = $_POST['logelak'];
$prezioa = $_POST['prezioa'];
$tamaina = $_POST['tamaina'];
$extrak = isset($_POST['extrak']) ? implode(',', $_POST['extrak']) : null;

$irudia = null;
if (isset($_FILES['irudia']) && $_FILES['irudia']['error'] === UPLOAD_ERR_OK) {
    $upload_dir = 'images/';
    $irudia = basename($_FILES['irudia']['name']);
    move_uploaded_file($_FILES['irudia']['tmp_name'], $upload_dir . $irudia);
}

$stmt = $mysqli->prepare("INSERT INTO Eraikuntza (mota, zonaldea, helbidea, logelak, prezioa, tamaina, extrak, irudia) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
$stmt->bind_param("ssssddss", $mota, $zonaldea, $helbidea, $logelak, $prezioa, $tamaina, $extrak, $irudia);

if ($stmt->execute()) {
    echo "Etxebizitza berria ongi gehitu da!<br>";
} else {
    echo "Errorea datuak gehitzean: " . $stmt->error . "<br>";
}

$stmt->close();
$mysqli->close();

header("Location: index.php");
exit();
?>
