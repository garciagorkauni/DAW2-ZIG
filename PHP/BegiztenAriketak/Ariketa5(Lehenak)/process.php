<!DOCTYPE html>
<html lang="eu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Znebaki Lehenak</title>
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
    <h1>Zenbaki lehenak</h1>
    <div class="container">
        <?php 
        if ($_POST["min"] == '' || $_POST["max"] == '' ) {
            echo "Zenbaki biak sartu behar dituzu.";
        } elseif ($_POST["min"] > $_POST["max"]){
            echo "Bigarren zenbakia handiagoa izan behar da.";
        } else {
            echo $_POST["min"] . ' eta ' . $_POST["max"] . ' zenbakien arteko zenbaki lehenak: <br>';
            echo calculateLehenak($_POST["min"], $_POST["max"]);
        }
        ?>
    
    </div>
    [<a href="./index.html" >ITZULI</a>]
</body>
<?php 
function calculateLehenak($min, $max) {
    $lehenak = '';
    
    for ($i=$min; $i <= $max ; $i++) { 
        if ($i % 2 !== 0) {
            $lehenak .= $i . ', ';
        }
    }

    return $lehenak;
}
?>
</html>
