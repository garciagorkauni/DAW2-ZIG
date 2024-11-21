<?php
session_start();

if (!isset($_SESSION['responses'])) {
    $_SESSION['responses'] = [
        "Bai" => 0,
        "Ez" => 0,
    ];
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['response'])) {
    $response = $_POST['response'];
    if (isset($_SESSION['responses'][$response])) {
        $_SESSION['responses'][$response]++;
    }
}

$totalVotes = array_sum($_SESSION['responses']);
?>
<!DOCTYPE html>
<html lang="eu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inkesta emaitzak</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
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
        .footer {
            margin-top: 20px;
            text-align: center;
        }
        .footer p {
            font-size: 12px;
            color: gray;
        }
    </style>
</head>
<body>
    <h1>Inkesta. Inkestaren emaitzak</h1>
    <div class="container">
        <p>Zure erantzuna erregistratu dugu.</p>
        <canvas id="resultsChart" width="400" height="400"></canvas>
        <p>Jasotako bozken guztira: <?php echo $totalVotes; ?></p>
        <p><a href="index.html">Bueltatu bozkatzeko orrira</a></p>
    </div>
    <div class="footer">
        <h3>PHP License</h3>
        <p>
            This program is free software; you can redistribute it and/or modify it under the terms of the PHP License 
            as published by the PHP Group and included in the distribution in the file: LICENSE.
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
    <script>
        const data = {
            labels: ["Bai", "Ez"],
            datasets: [{
                label: 'Bozkak',
                data: [
                    <?php echo $_SESSION['responses']['Bai']; ?>,
                    <?php echo $_SESSION['responses']['Ez']; ?>,
                ],
                backgroundColor: ['#4CAF50', '#F44336', '#FFC107']
            }]
        };

        const config = {
            type: 'pie',
            data: data
        };

        new Chart(document.getElementById('resultsChart'), config);
    </script>
</body>
</html>
