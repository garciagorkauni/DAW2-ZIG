<!DOCTYPE html>
<html lang="eu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zenbakiaren Faktoriala Kalkulatu</title>
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
    <h1>Zenbakiaren faktoriala</h1>
    <div class="container">
        <?php 
        if ($_POST["number"] == '') {
            echo "Zenbaki bat sartu behar duzu";
        } else {
            echo '<p>Zenbakia: ' . $_POST["number"] . '</p><br>';
            echo '<p>Faktoriala: ' . calculateFactorial($_POST["number"]) . '</p><br>';
        }
        ?>
    
    </div>
    [<a href="./index.html" >ITZULI</a>]
</body>
<?php 
function calculateFactorial($number) {
    $factorial = 1;
    for($i=$number; $i > 0 ; $i--){ 
        $factorial *= $i;
    }

    return $factorial;
}
?>
</html>
