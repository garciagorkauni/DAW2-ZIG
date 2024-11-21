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
    <h1>Irudien azalera</h1>
    <div class="container">
        <?php 
        if ($_POST["dimension"] == '') {
            echo "Zenbaki bat sartu behar duzu";
        } else {
            echo 'Zure area ' . calculateArea($_POST["shape"], $_POST["dimension"]) . ' da.';
        }
        ?>
    
    </div>
    [<a href="./index.html" >ITZULI</a>]
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
function calculateArea($shape, $dimension) {
    switch ($shape) {
        case 'triangle':
            $height = $dimension;
            $area = ($dimension * $height) / 2;
            return $area;

        case 'square':
            $area = $dimension * $dimension;
            return $area;

        case 'circle':
            $area = pi() * pow($dimension, 2);
            return $area;
    }
}
?>
</html>
