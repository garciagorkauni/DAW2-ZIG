<!DOCTYPE html>
<html lang="eu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Irudien Azalera Kalkulatu</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        h1 {
            color: blue;
            text-align: center;
        }
        .container {
            width: 50%;
            margin: 20px auto;
            border: 1px solid #000;
            padding: 20px;
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        select, input[type="number"], button {
            padding: 5px;
            font-size: 16px;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
        }
        .footer p {
            font-size: 12px;
            color: gray;
        }
    </style>
</head>
<body>
    <h1>Formularioaren emaitza</h1>
    <div class="container">
        <p>Berroa ondo jaso da:</p>
        <ul>
            <li>Izenburura: <?php echo $_POST["title"] ?></li>
            <li>Testua: <?php echo $_POST["content"] ?></li>
            <li>Kategoria: <?php echo $_POST["type"] ?></li>
            <li>Irudia: <?php echo $_FILES["image"]["tmp_name"] ?></li>
        </ul>

    </div>
    [<a href="./index.html" >Beste berri bat gehitu</a>]
    <div class="footer">
        <h3>PHP License</h3>
        <p>
            This program is free software; you can redistribute it and/or modify it under the terms of the PHP License 
            as published by the PHP Group and included in the distribution in the file: LICENSE
        </p>
        <p>
            This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the 
            implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
        </p>
        <p>
            If you did not receive a copy of the PHP license, or have any questions about PHP licensing, 
            please contact license@php.net.
        </p>
    </div>
</body>
<?php 
function calculateArea($conversion, $euro) {
    switch ($conversion) {
        case 'dolar':
            return $euro * 1.05;

        case 'libera':
            return $euro * 0.84;

        case 'yen':
            return $euro * 163.49;

        case 'franko':
            return $euro * 0.94;
    }
}
?>
</html>
